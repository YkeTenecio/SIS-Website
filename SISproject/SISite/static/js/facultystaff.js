/* facultystaff.js — live search for faculty, affiliates, staff */

(function () {

  const departmentAliases = {
    'environmental science':   ['envi', 'environment', 'environmental', 'environmental science'],
    'sustainable development': ['sds', 'sustainable', 'sustainable development', 'development studies'],
    'data science':            ['ds', 'data', 'data science', 'datasci'],
  };

  function matchesName(cardName, query) {
    const words = cardName.toLowerCase().split(/\s+/);
    return words.some(function (word) { return word.startsWith(query); });
  }

  function matchesDepartment(cardDept, query) {
    for (const dept in departmentAliases) {
      if (cardDept.includes(dept)) {
        return departmentAliases[dept].some(function (alias) {
          return alias.startsWith(query);
        });
      }
    }
    return false;
  }

  /* ── Standard search (Faculty and Staff pages) ── */
  function initSearch(inputId, gridId) {
    const input = document.getElementById(inputId);
    const grid  = document.getElementById(gridId);
    if (!input || !grid) return;

    input.addEventListener('input', function () {
      const query = this.value.trim().toLowerCase();

      grid.querySelectorAll('.faculty-card').forEach(function (card) {
        if (query === '') {
          card.classList.remove('hidden');
          return;
        }
        const name = card.dataset.name || '';
        const dept = card.dataset.department || '';
        const show = matchesName(name, query) || matchesDepartment(dept, query);
        card.classList.toggle('hidden', !show);
      });
    });
  }

  /* ── Affiliates search — switches between sectioned and flat view ── */
  function initAffiliatesSearch() {
    const input     = document.getElementById('affiliatesSearch');
    const sectioned = document.getElementById('affiliatesSectioned');
    const flatGrid  = document.getElementById('affiliatesGrid');
    if (!input || !sectioned || !flatGrid) return;

    input.addEventListener('input', function () {
      const query = this.value.trim().toLowerCase();

      if (query === '') {
        // Restore sectioned view
        sectioned.style.display = '';
        flatGrid.style.display  = 'none';
        // Clear any hidden state on flat grid cards
        flatGrid.querySelectorAll('.faculty-card').forEach(function (card) {
          card.classList.remove('hidden');
        });
        return;
      }

      // Switch to flat view and filter
      sectioned.style.display = 'none';
      flatGrid.style.display  = '';

      flatGrid.querySelectorAll('.faculty-card').forEach(function (card) {
        const name = card.dataset.name || '';
        const dept = card.dataset.department || '';
        const show = matchesName(name, query) || matchesDepartment(dept, query);
        card.classList.toggle('hidden', !show);
      });
    });
  }

  /* Initialise — each function safely skips if IDs aren't on the page */
  initSearch('facultySearch', 'facultyGrid');
  initSearch('staffSearch',   'staffGrid');
  initAffiliatesSearch();

})();