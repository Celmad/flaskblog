
// ** DARK/LIGHT THEM IMPLEMENTATION **
const THEME_TOGGLE = document.getElementById('theme-toggle');
const BODY = document.body;
const SIDEBAR_ITEMS = document.getElementsByClassName('sidebar-items');
const THEME_ICON = document.getElementById('theme-icon');
const PAGE_HEADING = document.getElementById('page-heading');
let articles = document.getElementsByClassName('content-section');
let articlesTitle = document.getElementsByClassName('article-title');

THEME_TOGGLE.addEventListener('input', (e) => {
    // debugger;
    
    const isChecked = e.target.checked;
    
	if(isChecked) {
        // Dark Theme
        BODY.classList.add('body-dark');
        BODY.classList.remove('body-light');
        THEME_ICON.classList.add('fa-moon');
        THEME_ICON.classList.remove('fa-sun');
        if (PAGE_HEADING != null) {
            PAGE_HEADING.classList.add('heading-dark-theme');
            PAGE_HEADING.classList.remove('heading-light-theme');
        }
        for (var i = 0; i < articles.length; i++) {
            article = articles[i];
            article.classList.add('article-dark');
            article.classList.remove('article-light');
        }
        for (var i = 0; i < articlesTitle.length; i++) {
            articleTitle = articlesTitle[i];
            articleTitle.classList.add('article-title-dark');
            articleTitle.classList.remove('article-title-light');
        }
        for (var i = 0; i < SIDEBAR_ITEMS.length; i++) {
            sidebarItem = SIDEBAR_ITEMS[i];
            sidebarItem.classList.add('sidebar-items-dark');
            sidebarItem.classList.remove('sidebar-items-light');
        }
	} else { 
        // Light Theme
        BODY.classList.add('body-light');
        BODY.classList.remove('body-dark');
        THEME_ICON.classList.add('fa-sun');
        THEME_ICON.classList.remove('fa-moon');
        if (PAGE_HEADING != null) {
            PAGE_HEADING.classList.add('heading-light-theme');
            PAGE_HEADING.classList.remove('heading-dark-theme');
        }
        for (var i = 0; i < articles.length; i++) {
            article = articles[i];
            article.classList.add('article-light');
            article.classList.remove('article-dark');
        }
        for (var i = 0; i < articlesTitle.length; i++) {
            articleTitle = articlesTitle[i];
            articleTitle.classList.add('article-title-light');
            articleTitle.classList.remove('article-title-dark');
        }
        for (var i = 0; i < SIDEBAR_ITEMS.length; i++) {
            sidebarItem = SIDEBAR_ITEMS[i];
            sidebarItem.classList.add('sidebar-items-light');
            sidebarItem.classList.remove('sidebar-items-dark');
        }
	}
});

// ** ACTIVE COLOURED NAVIGATION
// const HOME_LINK = document.getElementById('home-link');
// const NEW_POST_LINK = document.getElementById('new-post-link');
// const ACCOUNT_LINK = document.getElementById('account-link');
// const LOGOUT_LINK = document.getElementById('logout-link');
// const ABOUT_LINK = document.getElementById('about-link');
// const LOGIN_LINK = document.getElementById('login-link');
// const REGISTER_LINK = document.getElementById('register-link');
