(function (window) {
  'use strict';
  const locale = (code, name, nativeName, labels, options) => Object.freeze({
    code, name, nativeName, dir: options && options.dir || 'ltr', route: code === 'en' ? '/' : `/${code}/`,
    websiteLanguage: code === 'en' ? 'complete_english_source' : 'governed_route_pending_human_review',
    productContentLanguage: code === 'en' ? 'complete_english_source' : 'not_released',
    checkoutLanguage: 'not_released', deliveryLanguage: 'not_released', supportLanguage: 'not_released', legalPolicyLanguage: 'not_released',
    priority: options && options.priority || null, requiresRtlQA: Boolean(options && options.requiresRtlQA),
    interfaceStatus: code === 'en' ? 'complete' : 'translated_navigation_pending_human_review', labels
  });
  const locales = Object.freeze([
    locale('en', 'English', 'English', { home: 'Home', library: 'Library', freeTools: 'Free tools', app: 'App Store', language: 'Language', selector: 'English', notice: 'English is the current complete website and product source language.' }, { priority: 0 }),
    locale('pt-BR', 'Portuguese (Brazil)', 'Português (Brasil)', { home: 'Início', library: 'Biblioteca', freeTools: 'Ferramentas gratuitas', app: 'App Store', language: 'Idioma', selector: 'Português (Brasil)', notice: 'Esta rota de idioma está preparada para revisão humana. O conteúdo completo do site e do produto permanece em inglês até a liberação.' }, { priority: 1 }),
    locale('es-419', 'Spanish (Latin America)', 'Español (Latinoamérica)', { home: 'Inicio', library: 'Biblioteca', freeTools: 'Herramientas gratuitas', app: 'App Store', language: 'Idioma', selector: 'Español (Latinoamérica)', notice: 'Esta ruta de idioma está preparada para revisión humana. El contenido completo del sitio y del producto sigue en inglés hasta su publicación.' }, { priority: 2 }),
    locale('fr', 'French', 'Français', { home: 'Accueil', library: 'Bibliothèque', freeTools: 'Outils gratuits', app: 'App Store', language: 'Langue', selector: 'Français', notice: 'Cette route linguistique est préparée pour une révision humaine. Le contenu complet du site et du produit reste en anglais jusqu’à sa publication.' }),
    locale('de', 'German', 'Deutsch', { home: 'Startseite', library: 'Bibliothek', freeTools: 'Kostenlose Tools', app: 'App Store', language: 'Sprache', selector: 'Deutsch', notice: 'Diese Sprachroute ist für die menschliche Prüfung vorbereitet. Vollständige Website- und Produktinhalte bleiben bis zur Freigabe auf Englisch.' }),
    locale('it', 'Italian', 'Italiano', { home: 'Home', library: 'Libreria', freeTools: 'Strumenti gratuiti', app: 'App Store', language: 'Lingua', selector: 'Italiano', notice: 'Questo percorso linguistico è pronto per la revisione umana. I contenuti completi del sito e del prodotto restano in inglese fino alla pubblicazione.' }),
    locale('ja', 'Japanese', '日本語', { home: 'ホーム', library: 'ライブラリ', freeTools: '無料ツール', app: 'App Store', language: '言語', selector: '日本語', notice: 'この言語ルートは人によるレビュー用に準備されています。完全なウェブサイトと製品コンテンツは公開まで英語のままです。' }),
    locale('ko', 'Korean', '한국어', { home: '홈', library: '라이브러리', freeTools: '무료 도구', app: 'App Store', language: '언어', selector: '한국어', notice: '이 언어 경로는 사람의 검토를 위해 준비되었습니다. 전체 웹사이트와 제품 콘텐츠는 출시 전까지 영어로 유지됩니다.' }),
    locale('zh-Hans', 'Chinese (Simplified)', '简体中文', { home: '首页', library: '资料库', freeTools: '免费工具', app: 'App Store', language: '语言', selector: '简体中文', notice: '此语言路径已为人工审核准备。完整的网站和产品内容在发布前仍保持英文。' }),
    locale('zh-Hant', 'Chinese (Traditional)', '繁體中文', { home: '首頁', library: '資料庫', freeTools: '免費工具', app: 'App Store', language: '語言', selector: '繁體中文', notice: '此語言路徑已為人工審核準備。完整的網站和產品內容在發布前仍保持英文。' }),
    locale('ar', 'Arabic', 'العربية', { home: 'الرئيسية', library: 'المكتبة', freeTools: 'أدوات مجانية', app: 'متجر التطبيقات', language: 'اللغة', selector: 'العربية', notice: 'تم إعداد مسار اللغة هذا للمراجعة البشرية. يبقى محتوى الموقع والمنتج الكامل باللغة الإنجليزية إلى حين الإطلاق.' }, { dir: 'rtl', requiresRtlQA: true }),
    locale('ru', 'Russian', 'Русский', { home: 'Главная', library: 'Библиотека', freeTools: 'Бесплатные инструменты', app: 'App Store', language: 'Язык', selector: 'Русский', notice: 'Этот языковой маршрут подготовлен для проверки человеком. Полный контент сайта и продукта остаётся на английском до выпуска.' }),
    locale('pl', 'Polish', 'Polski', { home: 'Strona główna', library: 'Biblioteka', freeTools: 'Bezpłatne narzędzia', app: 'App Store', language: 'Język', selector: 'Polski', notice: 'Ta ścieżka językowa jest przygotowana do weryfikacji przez człowieka. Pełna treść strony i produktu pozostaje po angielsku do czasu wydania.' }),
    locale('nl', 'Dutch', 'Nederlands', { home: 'Home', library: 'Bibliotheek', freeTools: 'Gratis hulpmiddelen', app: 'App Store', language: 'Taal', selector: 'Nederlands', notice: 'Deze taalroute is voorbereid voor menselijke beoordeling. Volledige website- en productinhoud blijft Engels tot de release.' })
  ]);
  const byCode = Object.freeze(Object.fromEntries(locales.map((item) => [item.code, item])));
  window.NORTH_LOCALES = Object.freeze({ sourceLocale: 'en', locales, byCode, priorityQueue: ['pt-BR', 'es-419'], routeFor: (code) => byCode[code] ? byCode[code].route : '/', isRtl: (code) => Boolean(byCode[code] && byCode[code].dir === 'rtl') });
})(window);
