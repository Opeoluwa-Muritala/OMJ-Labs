const account = "Opeoluwa-Muritala";
const projects = [...document.querySelectorAll(".project-card")];
const githubStatus = document.getElementById("github-status");
const filterBar = document.getElementById("project-filters");

document.getElementById("year").textContent = String(new Date().getFullYear());

if (filterBar) {
  const filters = [...filterBar.querySelectorAll("button[data-filter]")];
  for (const button of filters) {
    button.addEventListener("click", () => {
      const selected = button.dataset.filter;
      for (const filter of filters) {
        const active = filter === button;
        filter.classList.toggle("is-active", active);
        filter.setAttribute("aria-pressed", String(active));
      }
      for (const project of projects) {
        const categories = (project.dataset.categories || "").split(/\s+/);
        project.hidden = selected !== "all" && !categories.includes(selected);
      }
    });
  }
  filterBar.hidden = false;
}

async function updateProjectMetadata() {
  try {
    const response = await fetch(`https://api.github.com/users/${account}/repos?type=owner&per_page=100&sort=updated`, {
      headers: { Accept: "application/vnd.github+json" },
      cache: "no-store"
    });
    if (!response.ok) throw new Error("GitHub data unavailable");
    const repositories = await response.json();
    if (!Array.isArray(repositories)) throw new Error("Unexpected GitHub response");
    const byName = new Map(repositories.map((repo) => [repo.name, repo]));
    let updated = 0;

    for (const project of projects) {
      const name = project.dataset.repo;
      if (!name) continue;
      const repo = byName.get(name);
      if (!repo || repo.private || repo.owner?.login !== account) continue;
      const meta = project.querySelector(".repo-meta");
      if (!meta) continue;
      const language = typeof repo.language === "string" && repo.language.length < 40 ? repo.language : "Project";
      const pushed = new Date(repo.pushed_at);
      const updateLabel = Number.isNaN(pushed.valueOf()) ? "GitHub" : `Updated ${new Intl.DateTimeFormat("en", { month: "short", year: "numeric" }).format(pushed)}`;
      meta.textContent = `${language} · ${updateLabel}`;
      updated += 1;
    }
    if (updated > 0) githubStatus.textContent = "Repository details updated from GitHub";
  } catch {
    githubStatus.textContent = "Curated project details";
  }
}

updateProjectMetadata();
