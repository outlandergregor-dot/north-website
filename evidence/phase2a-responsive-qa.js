async (page) => {
  const base = 'http://localhost:4173';
  const pages = [
    ['/library', 'library'],
    ['/library/resources', 'resources'],
    ['/library/programs', 'programs'],
    ['/library/books', 'books'],
    ['/library/item?product=1-3-5-execution-planner', 'execution-planner'],
    ['/library/item?product=decision-clarity-toolkit', 'decision-toolkit'],
    ['/library/item?product=focus-recovery-program', 'focus-program'],
    ['/library/item?product=find-your-north-book', 'concept-book'],
    ['/internal/studio-control.html', 'readiness-dashboard']
  ];
  const results = [];
  for (const [route, name] of pages) {
    for (const [width, height, mode] of [[390, 844, 'mobile'], [1440, 1000, 'desktop']]) {
      await page.setViewportSize({ width, height });
      await page.goto(base + route, { waitUntil: 'networkidle' });
      await page.evaluate(() => { document.body.style.zoom = ''; });
      const metrics = await page.evaluate(() => ({
        width: window.innerWidth,
        scrollWidth: document.documentElement.scrollWidth,
        overflow: document.documentElement.scrollWidth > window.innerWidth + 1,
        title: document.title,
        anchors: document.querySelectorAll('a').length,
        commerceLinks: Array.from(document.querySelectorAll('a')).filter((link) => /checkout|purchase|cart|payment|gumroad|stripe|paypal/i.test(`${link.href} ${link.textContent}`)).map((link) => link.textContent.trim())
      }));
      results.push({ name, route, mode, ...metrics });
    }
  }
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto(base + '/library', { waitUntil: 'networkidle' });
  await page.keyboard.press('Tab');
  const keyboard = await page.evaluate(() => ({
    firstFocusedTag: document.activeElement?.tagName || null,
    firstFocusedText: document.activeElement?.textContent?.trim().slice(0, 80) || null,
    outlineStyle: getComputedStyle(document.activeElement).outlineStyle,
    outlineWidth: getComputedStyle(document.activeElement).outlineWidth
  }));
  const zoomResults = [];
  for (const [route, name] of [['/library', 'library'], ['/internal/studio-control.html', 'readiness-dashboard']]) {
    await page.setViewportSize({ width: 320, height: 844 });
    await page.goto(base + route, { waitUntil: 'networkidle' });
    zoomResults.push(await page.evaluate(() => ({
      route: location.pathname,
      width: window.innerWidth,
      scrollWidth: document.documentElement.scrollWidth,
      overflow: document.documentElement.scrollWidth > window.innerWidth + 1
    })));
  }
  return { result: results.every((item) => !item.overflow && item.commerceLinks.length === 0) && zoomResults.every((item) => !item.overflow) && keyboard.firstFocusedTag === 'A' ? 'PASS' : 'FAIL', routes: results, keyboard, zoom: zoomResults };
}
