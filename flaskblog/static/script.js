const THEME_TOGGLE = document.getElementById('theme-toggle');
const BODY = document.body;
let articles = document.getElementsByClassName('content-section');
let articlesTitle = document.getElementsByClassName('article-title');
let sidebarItems = document.getElementsByClassName('sidebar-items');
let themeIcon = document.getElementById('theme-icon');

THEME_TOGGLE.addEventListener('input', (e) => {
    // debugger;
    
    const isChecked = e.target.checked;
    
	if(isChecked) {
        BODY.classList.add('body-dark');
        BODY.classList.remove('body-light');
        themeIcon.classList.add('fa-moon');
        themeIcon.classList.remove('fa-sun');
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
        for (var i = 0; i < sidebarItems.length; i++) {
            sidebarItem = sidebarItems[i];
            sidebarItem.classList.add('sidebar-items-dark');
            sidebarItem.classList.remove('sidebar-items-light');
        }
        
	} else {
        BODY.classList.add('body-light');
        BODY.classList.remove('body-dark');
        themeIcon.classList.add('fa-sun');
        themeIcon.classList.remove('fa-moon');
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
        for (var i = 0; i < sidebarItems.length; i++) {
            sidebarItem = sidebarItems[i];
            sidebarItem.classList.add('sidebar-items-light');
            sidebarItem.classList.remove('sidebar-items-dark');
        }
	}
});