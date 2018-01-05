<!DOCTYPE html>
<html class="" lang="en">
<head prefix="og: http://ogp.me/ns#">
<meta charset="utf-8">
<meta content="IE=edge" http-equiv="X-UA-Compatible">
<meta content="object" property="og:type">
<meta content="GitLab" property="og:site_name">
<meta content="primitive_interfaces/base.py · master · datadrivendiscovery / primitive-interfaces" property="og:title">
<meta content="Python interfaces for TA1 primitives." property="og:description">
<meta content="https://assets.gitlab-static.net/assets/gitlab_logo-7ae504fe4f68fdebb3c2034e36621930cd36ea87924c11ff65dbcb8ed50dca58.png" property="og:image">
<meta content="64" property="og:image:width">
<meta content="64" property="og:image:height">
<meta content="https://gitlab.com/datadrivendiscovery/primitive-interfaces/blob/master/primitive_interfaces/base.py" property="og:url">
<meta content="summary" property="twitter:card">
<meta content="primitive_interfaces/base.py · master · datadrivendiscovery / primitive-interfaces" property="twitter:title">
<meta content="Python interfaces for TA1 primitives." property="twitter:description">
<meta content="https://assets.gitlab-static.net/assets/gitlab_logo-7ae504fe4f68fdebb3c2034e36621930cd36ea87924c11ff65dbcb8ed50dca58.png" property="twitter:image">

<title>primitive_interfaces/base.py · master · datadrivendiscovery / primitive-interfaces · GitLab</title>
<meta content="Python interfaces for TA1 primitives." name="description">
<link rel="shortcut icon" type="image/x-icon" href="https://assets.gitlab-static.net/assets/favicon-075eba76312e8421991a0c1f89a89ee81678bcde72319dd3e8047e2a47cd3a42.ico" id="favicon" />
<link rel="stylesheet" media="all" href="https://assets.gitlab-static.net/assets/application-476f4ca22df7463aa2be1f4d700a3f15408ec4787790db6700d7e213122656ba.css" />
<link rel="stylesheet" media="print" href="https://assets.gitlab-static.net/assets/print-74b3d49adeaada27337e759b75a34af7cf3d80051de91d60d40570f5a382e132.css" />


<script>
//<![CDATA[
window.gon={};gon.api_version="v4";gon.default_avatar_url="https:\/\/assets.gitlab-static.net\/assets\/no_avatar-849f9c04a3a0d0cea2424ae97b27447dc64a7dbfae83c036c45b403392f0e8ba.png";gon.max_file_size=10;gon.asset_host="https:\/\/assets.gitlab-static.net";gon.webpack_public_path="https:\/\/assets.gitlab-static.net\/assets\/webpack\/";gon.relative_url_root="";gon.shortcuts_path="\/help\/shortcuts";gon.user_color_scheme="white";gon.katex_css_url="https:\/\/assets.gitlab-static.net\/assets\/katex-dc07578acd203b2dd73a8c78cdb8dcb79144ba11a23749d80904496b7ff8a650.css";gon.katex_js_url="https:\/\/assets.gitlab-static.net\/assets\/katex-04bcf56379fcda0ee7c7a63f71d0fc15ffd2e014d017cd9d51fd6554dfccf40a.js";gon.sentry_dsn="https:\/\/526a2f38a53d44e3a8e69bfa001d1e8b@sentry.gitlap.com\/15";gon.gitlab_url="https:\/\/gitlab.com";gon.revision="3f64be9";gon.gitlab_logo="https:\/\/assets.gitlab-static.net\/assets\/gitlab_logo-7ae504fe4f68fdebb3c2034e36621930cd36ea87924c11ff65dbcb8ed50dca58.png";gon.sprite_icons="https:\/\/gitlab.com\/assets\/icons-e18ff9bb200a2eb092fb610d1592af76d420722d4d8b7d48d6b20c7911bf532a.svg";gon.current_user_id=1889626;gon.current_username="azunre";gon.current_user_fullname="Paul Azunre";gon.current_user_avatar_url="\/uploads\/-\/system\/user\/avatar\/1889626\/avatar.png";
//]]>
</script>

<script src="https://assets.gitlab-static.net/assets/webpack/webpack_runtime.6ffd9e931a10db945284.bundle.js" defer="defer"></script>
<script src="https://assets.gitlab-static.net/assets/webpack/common.e6aa5ea346b7e04f6c75.bundle.js" defer="defer"></script>
<script src="https://assets.gitlab-static.net/assets/webpack/main.ce3e5cbca657cef79611.bundle.js" defer="defer"></script>
<script src="https://assets.gitlab-static.net/assets/webpack/raven.c94699aec8e665da5599.bundle.js" defer="defer"></script>


<script src="https://assets.gitlab-static.net/assets/webpack/blob.451528c644c00014c31a.bundle.js" defer="defer"></script>

<script>
  window.uploads_path = "/datadrivendiscovery/primitive-interfaces/uploads";
</script>

<meta name="csrf-param" content="authenticity_token" />
<meta name="csrf-token" content="9GHtgNzpl/yVmA76V0Br94ZKmj++hq9qSgRSC5iRa4Q7gEE/NO6C16r/AlJNooNiAkQHdaxtOtIUkqUvqVF4Xg==" />
<meta content="origin-when-cross-origin" name="referrer">
<meta content="width=device-width, initial-scale=1, maximum-scale=1" name="viewport">
<meta content="#474D57" name="theme-color">
<link rel="apple-touch-icon" type="image/x-icon" href="https://assets.gitlab-static.net/assets/touch-icon-iphone-5a9cee0e8a51212e70b90c87c12f382c428870c0ff67d1eb034d884b78d2dae7.png" />
<link rel="apple-touch-icon" type="image/x-icon" href="https://assets.gitlab-static.net/assets/touch-icon-ipad-a6eec6aeb9da138e507593b464fdac213047e49d3093fc30e90d9a995df83ba3.png" sizes="76x76" />
<link rel="apple-touch-icon" type="image/x-icon" href="https://assets.gitlab-static.net/assets/touch-icon-iphone-retina-72e2aadf86513a56e050e7f0f2355deaa19cc17ed97bbe5147847f2748e5a3e3.png" sizes="120x120" />
<link rel="apple-touch-icon" type="image/x-icon" href="https://assets.gitlab-static.net/assets/touch-icon-ipad-retina-8ebe416f5313483d9c1bc772b5bbe03ecad52a54eba443e5215a22caed2a16a2.png" sizes="152x152" />
<link color="rgb(226, 67, 41)" href="https://assets.gitlab-static.net/assets/logo-d36b5212042cebc89b96df4bf6ac24e43db316143e89926c0db839ff694d2de4.svg" rel="mask-icon">
<meta content="https://assets.gitlab-static.net/assets/msapplication-tile-1196ec67452f618d39cdd85e2e3a542f76574c071051ae7effbfde01710eb17d.png" name="msapplication-TileImage">
<meta content="#30353E" name="msapplication-TileColor">



</head>

<body class="ui_indigo " data-find-file="/datadrivendiscovery/primitive-interfaces/find_file/master" data-group="" data-page="projects:blob:show" data-project="primitive-interfaces">


<header class="navbar navbar-gitlab navbar-gitlab-new">
<a class="sr-only gl-accessibility" href="#content-body" tabindex="1">Skip to content</a>
<div class="container-fluid">
<div class="header-content">
<div class="title-container">
<h1 class="title">
<a title="Dashboard" id="logo" href="/"><svg width="24" height="24" class="tanuki-logo" viewBox="0 0 36 36">
  <path class="tanuki-shape tanuki-left-ear" fill="#e24329" d="M2 14l9.38 9v-9l-4-12.28c-.205-.632-1.176-.632-1.38 0z"/>
  <path class="tanuki-shape tanuki-right-ear" fill="#e24329" d="M34 14l-9.38 9v-9l4-12.28c.205-.632 1.176-.632 1.38 0z"/>
  <path class="tanuki-shape tanuki-nose" fill="#e24329" d="M18,34.38 3,14 33,14 Z"/>
  <path class="tanuki-shape tanuki-left-eye" fill="#fc6d26" d="M18,34.38 11.38,14 2,14 6,25Z"/>
  <path class="tanuki-shape tanuki-right-eye" fill="#fc6d26" d="M18,34.38 24.62,14 34,14 30,25Z"/>
  <path class="tanuki-shape tanuki-left-cheek" fill="#fca326" d="M2 14L.1 20.16c-.18.565 0 1.2.5 1.56l17.42 12.66z"/>
  <path class="tanuki-shape tanuki-right-cheek" fill="#fca326" d="M34 14l1.9 6.16c.18.565 0 1.2-.5 1.56L18 34.38z"/>
</svg>

<span class="logo-text hidden-xs">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 617 169"><path d="M315.26 2.97h-21.8l.1 162.5h88.3v-20.1h-66.5l-.1-142.4M465.89 136.95c-5.5 5.7-14.6 11.4-27 11.4-16.6 0-23.3-8.2-23.3-18.9 0-16.1 11.2-23.8 35-23.8 4.5 0 11.7.5 15.4 1.2v30.1h-.1m-22.6-98.5c-17.6 0-33.8 6.2-46.4 16.7l7.7 13.4c8.9-5.2 19.8-10.4 35.5-10.4 17.9 0 25.8 9.2 25.8 24.6v7.9c-3.5-.7-10.7-1.2-15.1-1.2-38.2 0-57.6 13.4-57.6 41.4 0 25.1 15.4 37.7 38.7 37.7 15.7 0 30.8-7.2 36-18.9l4 15.9h15.4v-83.2c-.1-26.3-11.5-43.9-44-43.9M557.63 149.1c-8.2 0-15.4-1-20.8-3.5V70.5c7.4-6.2 16.6-10.7 28.3-10.7 21.1 0 29.2 14.9 29.2 39 0 34.2-13.1 50.3-36.7 50.3m9.2-110.6c-19.5 0-30 13.3-30 13.3v-21l-.1-27.8h-21.3l.1 158.5c10.7 4.5 25.3 6.9 41.2 6.9 40.7 0 60.3-26 60.3-70.9-.1-35.5-18.2-59-50.2-59M77.9 20.6c19.3 0 31.8 6.4 39.9 12.9l9.4-16.3C114.5 6 97.3 0 78.9 0 32.5 0 0 28.3 0 85.4c0 59.8 35.1 83.1 75.2 83.1 20.1 0 37.2-4.7 48.4-9.4l-.5-63.9V75.1H63.6v20.1h38l.5 48.5c-5 2.5-13.6 4.5-25.3 4.5-32.2 0-53.8-20.3-53.8-63-.1-43.5 22.2-64.6 54.9-64.6M231.43 2.95h-21.3l.1 27.3v94.3c0 26.3 11.4 43.9 43.9 43.9 4.5 0 8.9-.4 13.1-1.2v-19.1c-3.1.5-6.4.7-9.9.7-17.9 0-25.8-9.2-25.8-24.6v-65h35.7v-17.8h-35.7l-.1-38.5M155.96 165.47h21.3v-124h-21.3v124M155.96 24.37h21.3V3.07h-21.3v21.3"/></svg>

</span>
</a></h1>
<ul class="list-unstyled navbar-sub-nav">
<li id="nav-projects-dropdown" class="home dropdown header-projects"><a data-toggle="dropdown" href="#">
Projects
<svg class=" caret-down"><use xlink:href="https://gitlab.com/assets/icons-e18ff9bb200a2eb092fb610d1592af76d420722d4d8b7d48d6b20c7911bf532a.svg#angle-down"></use></svg>
</a>
<div class="dropdown-menu projects-dropdown-menu">
<div class="projects-dropdown-container">
<div class="project-dropdown-sidebar">
<ul>
<li class=""><a href="/dashboard/projects">Your projects
</a></li><li class=""><a href="/dashboard/projects/starred">Starred projects
</a></li><li class=""><a href="/explore">Explore projects
</a></li></ul>
</div>
<div class="project-dropdown-content">
<div data-project-id="4662462" data-project-name="primitive-interfaces" data-project-namespace="datadrivendiscovery / primitive-interfaces" data-project-web-url="https://gitlab.com/datadrivendiscovery/primitive-interfaces" data-user-name="azunre" id="js-projects-dropdown"></div>
</div>
</div>

</div>
</li><li class="hidden-xs"><a class="dashboard-shortcuts-groups" title="Groups" href="/dashboard/groups">Groups
</a></li><li class="visible-lg"><a class="dashboard-shortcuts-activity" title="Activity" href="/dashboard/activity">Activity
</a></li><li class="visible-lg"><a class="dashboard-shortcuts-milestones" title="Milestones" href="/dashboard/milestones">Milestones
</a></li><li class="visible-lg"><a class="dashboard-shortcuts-snippets" title="Snippets" href="/dashboard/snippets">Snippets
</a></li><li class="header-more dropdown hidden-lg">
<a data-toggle="dropdown" href="#">
More
<svg class=" caret-down"><use xlink:href="https://gitlab.com/assets/icons-e18ff9bb200a2eb092fb610d1592af76d420722d4d8b7d48d6b20c7911bf532a.svg#angle-down"></use></svg>
</a>
<div class="dropdown-menu">
<ul>
<li class="visible-xs"><a class="dashboard-shortcuts-groups" title="Groups" href="/dashboard/groups">Groups
</a></li><li class=""><a title="Activity" href="/dashboard/activity">Activity
</a></li><li class=""><a class="dashboard-shortcuts-milestones" title="Milestones" href="/dashboard/milestones">Milestones
</a></li><li class=""><a class="dashboard-shortcuts-snippets" title="Snippets" href="/dashboard/snippets">Snippets
</a></li></ul>
</div>
</li>
<li class="hidden">
<a title="Projects" class="dashboard-shortcuts-projects" href="/dashboard/projects">Projects
</a></li>
</ul>

</div>
<div class="navbar-collapse collapse">
<ul class="nav navbar-nav">
<li class="header-new dropdown">
<a class="header-new-dropdown-toggle has-tooltip" title="New..." ref="tooltip" aria-label="New..." data-toggle="dropdown" data-placement="bottom" data-container="body" href="/projects/new"><svg class="s16"><use xlink:href="https://gitlab.com/assets/icons-e18ff9bb200a2eb092fb610d1592af76d420722d4d8b7d48d6b20c7911bf532a.svg#plus-square"></use></svg>
<svg class=" caret-down"><use xlink:href="https://gitlab.com/assets/icons-e18ff9bb200a2eb092fb610d1592af76d420722d4d8b7d48d6b20c7911bf532a.svg#angle-down"></use></svg>
</a><div class="dropdown-menu-nav dropdown-menu-align-right">
<ul>
<li class="dropdown-bold-header">This project</li>
<li>
<a href="/datadrivendiscovery/primitive-interfaces/issues/new">New issue</a>
</li>
<li class="divider"></li>
<li class="dropdown-bold-header">GitLab</li>
<li>
<a href="/projects/new">New project</a>
</li>
<li>
<a href="/groups/new">New group</a>
</li>
<li>
<a href="/snippets/new">New snippet</a>
</li>
</ul>
</div>
</li>

<li class="hidden-sm hidden-xs">
<div class="has-location-badge search search-form">
<form class="navbar-form" action="/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" /><div class="search-input-container">
<div class="location-badge">This project</div>
<div class="search-input-wrap">
<div class="dropdown" data-url="/search/autocomplete">
<input type="search" name="search" id="search" placeholder="Search" class="search-input dropdown-menu-toggle no-outline js-search-dashboard-options" spellcheck="false" tabindex="1" autocomplete="off" data-toggle="dropdown" data-issues-path="/dashboard/issues" data-mr-path="/dashboard/merge_requests" aria-label="Search" />
<div class="dropdown-menu dropdown-select">
<div class="dropdown-content"><ul>
<li class="dropdown-menu-empty-item">
<a>
Loading...
</a>
</li>
</ul>
</div><div class="dropdown-loading"><i aria-hidden="true" data-hidden="true" class="fa fa-spinner fa-spin"></i></div>
</div>
<svg class="s16 search-icon"><use xlink:href="https://gitlab.com/assets/icons-e18ff9bb200a2eb092fb610d1592af76d420722d4d8b7d48d6b20c7911bf532a.svg#search"></use></svg>
<svg class="s16 clear-icon js-clear-input"><use xlink:href="https://gitlab.com/assets/icons-e18ff9bb200a2eb092fb610d1592af76d420722d4d8b7d48d6b20c7911bf532a.svg#close"></use></svg>
</div>
</div>
</div>
<input type="hidden" name="group_id" id="group_id" class="js-search-group-options" />
<input type="hidden" name="project_id" id="search_project_id" value="4662462" class="js-search-project-options" data-project-path="primitive-interfaces" data-name="primitive-interfaces" data-issues-path="/datadrivendiscovery/primitive-interfaces/issues" data-mr-path="/datadrivendiscovery/primitive-interfaces/merge_requests" data-issues-disabled="false" />
<input type="hidden" name="search_code" id="search_code" value="true" />
<input type="hidden" name="repository_ref" id="repository_ref" value="master" />

<div class="search-autocomplete-opts hide" data-autocomplete-path="/search/autocomplete" data-autocomplete-project-id="4662462" data-autocomplete-project-ref="master"></div>
</form></div>

</li>
<li class="visible-sm-inline-block visible-xs-inline-block">
<a title="Search" aria-label="Search" data-toggle="tooltip" data-placement="bottom" data-container="body" href="/search"><svg class="s16"><use xlink:href="https://gitlab.com/assets/icons-e18ff9bb200a2eb092fb610d1592af76d420722d4d8b7d48d6b20c7911bf532a.svg#search"></use></svg>
</a></li>
<li class="user-counter"><a title="Issues" class="dashboard-shortcuts-issues" aria-label="Issues" data-toggle="tooltip" data-placement="bottom" data-container="body" href="/dashboard/issues?assignee_id=1889626"><svg class="s16"><use xlink:href="https://gitlab.com/assets/icons-e18ff9bb200a2eb092fb610d1592af76d420722d4d8b7d48d6b20c7911bf532a.svg#issues"></use></svg>
<span class="badge hidden issues-count">
0
</span>
</a></li><li class="user-counter"><a title="Merge requests" class="dashboard-shortcuts-merge_requests" aria-label="Merge requests" data-toggle="tooltip" data-placement="bottom" data-container="body" href="/dashboard/merge_requests?assignee_id=1889626"><svg class="s16"><use xlink:href="https://gitlab.com/assets/icons-e18ff9bb200a2eb092fb610d1592af76d420722d4d8b7d48d6b20c7911bf532a.svg#git-merge"></use></svg>
<span class="badge hidden merge-requests-count">
0
</span>
</a></li><li class="user-counter"><a title="Todos" aria-label="Todos" class="shortcuts-todos" data-toggle="tooltip" data-placement="bottom" data-container="body" href="/dashboard/todos"><svg class="s16"><use xlink:href="https://gitlab.com/assets/icons-e18ff9bb200a2eb092fb610d1592af76d420722d4d8b7d48d6b20c7911bf532a.svg#todo-done"></use></svg>
<span class="badge hidden todos-count">
0
</span>
</a></li><li class="header-user dropdown">
<a class="header-user-dropdown-toggle" data-toggle="dropdown" href="/azunre"><img width="23" height="23" class="header-user-avatar lazy" data-src="https://assets.gitlab-static.net/uploads/-/system/user/avatar/1889626/avatar.png" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" />
<svg class=" caret-down"><use xlink:href="https://gitlab.com/assets/icons-e18ff9bb200a2eb092fb610d1592af76d420722d4d8b7d48d6b20c7911bf532a.svg#angle-down"></use></svg>
</a><div class="dropdown-menu-nav dropdown-menu-align-right">
<ul>
<li class="current-user">
<div class="user-name bold">
Paul Azunre
</div>
@azunre
</li>
<li class="divider"></li>
<li>
<a class="profile-link" data-user="azunre" href="/azunre">Profile</a>
</li>
<li>
<a href="/profile">Settings</a>
</li>
<li>
<a href="/help">Help</a>
</li>
<li class="divider"></li>
<li>
<a class="sign-out-link" href="/users/sign_out">Sign out</a>
</li>
</ul>
</div>
</li>
</ul>
</div>
<button class="navbar-toggle hidden-sm hidden-md hidden-lg" type="button">
<span class="sr-only">Toggle navigation</span>
<svg class="s12 more-icon js-navbar-toggle-right"><use xlink:href="https://gitlab.com/assets/icons-e18ff9bb200a2eb092fb610d1592af76d420722d4d8b7d48d6b20c7911bf532a.svg#more"></use></svg>
<svg class="s12 close-icon js-navbar-toggle-left"><use xlink:href="https://gitlab.com/assets/icons-e18ff9bb200a2eb092fb610d1592af76d420722d4d8b7d48d6b20c7911bf532a.svg#close"></use></svg>
</button>
</div>
</div>
</header>

<div class="page-with-contextual-sidebar page-with-sidebar">
<div class="nav-sidebar">
<div class="nav-sidebar-inner-scroll">
<div class="context-header">
<a title="primitive-interfaces" href="/datadrivendiscovery/primitive-interfaces"><div class="avatar-container s40 project-avatar">
<div class="avatar s40 avatar-tile identicon" style="background-color: #FFEBEE; color: #555">P</div>
</div>
<div class="sidebar-context-title">
primitive-interfaces
</div>
</a></div>
<ul class="sidebar-top-level-items">
<li class="home"><a class="shortcuts-project" href="/datadrivendiscovery/primitive-interfaces"><div class="nav-icon-container">
<svg><use xlink:href="https://gitlab.com/assets/icons-e18ff9bb200a2eb092fb610d1592af76d420722d4d8b7d48d6b20c7911bf532a.svg#project"></use></svg>
</div>
<span class="nav-item-name">
Overview
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><a href="/datadrivendiscovery/primitive-interfaces"><strong class="fly-out-top-item-name">
Overview
</strong>
</a></li><li class="divider fly-out-top-item"></li>
<li class=""><a title="Project details" class="shortcuts-project" href="/datadrivendiscovery/primitive-interfaces"><span>Details</span>
</a></li><li class=""><a title="Activity" class="shortcuts-project-activity" href="/datadrivendiscovery/primitive-interfaces/activity"><span>Activity</span>
</a></li><li class=""><a title="Cycle Analytics" class="shortcuts-project-cycle-analytics" href="/datadrivendiscovery/primitive-interfaces/cycle_analytics"><span>Cycle Analytics</span>
</a></li></ul>
</li><li class="active"><a class="shortcuts-tree" href="/datadrivendiscovery/primitive-interfaces/tree/master"><div class="nav-icon-container">
<svg><use xlink:href="https://gitlab.com/assets/icons-e18ff9bb200a2eb092fb610d1592af76d420722d4d8b7d48d6b20c7911bf532a.svg#doc_text"></use></svg>
</div>
<span class="nav-item-name">
Repository
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item active"><a href="/datadrivendiscovery/primitive-interfaces/tree/master"><strong class="fly-out-top-item-name">
Repository
</strong>
</a></li><li class="divider fly-out-top-item"></li>
<li class="active"><a href="/datadrivendiscovery/primitive-interfaces/tree/master">Files
</a></li><li class=""><a href="/datadrivendiscovery/primitive-interfaces/commits/master">Commits
</a></li><li class=""><a href="/datadrivendiscovery/primitive-interfaces/branches">Branches
</a></li><li class=""><a href="/datadrivendiscovery/primitive-interfaces/tags">Tags
</a></li><li class=""><a href="/datadrivendiscovery/primitive-interfaces/graphs/master">Contributors
</a></li><li class=""><a href="/datadrivendiscovery/primitive-interfaces/network/master">Graph
</a></li><li class=""><a href="/datadrivendiscovery/primitive-interfaces/compare?from=devel&amp;to=master">Compare
</a></li><li class=""><a href="/datadrivendiscovery/primitive-interfaces/graphs/master/charts">Charts
</a></li><li class=""><a href="/datadrivendiscovery/primitive-interfaces/path_locks">Locked Files
</a></li></ul>
</li><li class=""><a class="shortcuts-issues" href="/datadrivendiscovery/primitive-interfaces/issues"><div class="nav-icon-container">
<svg><use xlink:href="https://gitlab.com/assets/icons-e18ff9bb200a2eb092fb610d1592af76d420722d4d8b7d48d6b20c7911bf532a.svg#issues"></use></svg>
</div>
<span class="nav-item-name">
Issues
</span>
<span class="badge count issue_counter">
9
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><a href="/datadrivendiscovery/primitive-interfaces/issues"><strong class="fly-out-top-item-name">
Issues
</strong>
<span class="badge count issue_counter fly-out-badge">
9
</span>
</a></li><li class="divider fly-out-top-item"></li>
<li class=""><a title="Issues" href="/datadrivendiscovery/primitive-interfaces/issues"><span>
List
</span>
</a></li><li class=""><a title="Boards" href="/datadrivendiscovery/primitive-interfaces/boards"><span>
Boards
</span>
</a></li><li class=""><a title="Labels" href="/datadrivendiscovery/primitive-interfaces/labels"><span>
Labels
</span>
</a></li><li class=""><a title="Service Desk" href="/datadrivendiscovery/primitive-interfaces/issues/service_desk"><span>Service Desk</span>
</a></li><li class=""><a title="Milestones" href="/datadrivendiscovery/primitive-interfaces/milestones"><span>
Milestones
</span>
</a></li></ul>
</li><li class=""><a class="shortcuts-merge_requests" href="/datadrivendiscovery/primitive-interfaces/merge_requests"><div class="nav-icon-container">
<svg><use xlink:href="https://gitlab.com/assets/icons-e18ff9bb200a2eb092fb610d1592af76d420722d4d8b7d48d6b20c7911bf532a.svg#git-merge"></use></svg>
</div>
<span class="nav-item-name">
Merge Requests
</span>
<span class="badge count merge_counter js-merge-counter">
0
</span>
</a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><a href="/datadrivendiscovery/primitive-interfaces/merge_requests"><strong class="fly-out-top-item-name">
Merge Requests
</strong>
<span class="badge count merge_counter js-merge-counter fly-out-badge">
0
</span>
</a></li></ul>
</li><li class=""><a class="shortcuts-pipelines" href="/datadrivendiscovery/primitive-interfaces/pipelines"><div class="nav-icon-container">
<svg><use xlink:href="https://gitlab.com/assets/icons-e18ff9bb200a2eb092fb610d1592af76d420722d4d8b7d48d6b20c7911bf532a.svg#pipeline"></use></svg>
</div>
<span class="nav-item-name">
CI / CD
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><a href="/datadrivendiscovery/primitive-interfaces/pipelines"><strong class="fly-out-top-item-name">
CI / CD
</strong>
</a></li><li class="divider fly-out-top-item"></li>
<li class=""><a title="Pipelines" class="shortcuts-pipelines" href="/datadrivendiscovery/primitive-interfaces/pipelines"><span>
Pipelines
</span>
</a></li><li class=""><a title="Jobs" class="shortcuts-builds" href="/datadrivendiscovery/primitive-interfaces/-/jobs"><span>
Jobs
</span>
</a></li><li class=""><a title="Schedules" class="shortcuts-builds" href="/datadrivendiscovery/primitive-interfaces/pipeline_schedules"><span>
Schedules
</span>
</a></li><li class=""><a title="Charts" class="shortcuts-pipelines-charts" href="/datadrivendiscovery/primitive-interfaces/pipelines/charts"><span>
Charts
</span>
</a></li></ul>
</li><li class=""><a title="Members" class="shortcuts-tree" href="/datadrivendiscovery/primitive-interfaces/settings/members"><div class="nav-icon-container">
<svg><use xlink:href="https://gitlab.com/assets/icons-e18ff9bb200a2eb092fb610d1592af76d420722d4d8b7d48d6b20c7911bf532a.svg#users"></use></svg>
</div>
<span class="nav-item-name">
Members
</span>
</a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><a href="/datadrivendiscovery/primitive-interfaces/project_members"><strong class="fly-out-top-item-name">
Members
</strong>
</a></li></ul>
</li><a class="toggle-sidebar-button js-toggle-sidebar" role="button" title="Toggle sidebar" type="button">
<svg class=" icon-angle-double-left"><use xlink:href="https://gitlab.com/assets/icons-e18ff9bb200a2eb092fb610d1592af76d420722d4d8b7d48d6b20c7911bf532a.svg#angle-double-left"></use></svg>
<svg class=" icon-angle-double-right"><use xlink:href="https://gitlab.com/assets/icons-e18ff9bb200a2eb092fb610d1592af76d420722d4d8b7d48d6b20c7911bf532a.svg#angle-double-right"></use></svg>
<span class="collapse-text">Collapse sidebar</span>
</a>
<button name="button" type="button" class="close-nav-button"><svg class="s16"><use xlink:href="https://gitlab.com/assets/icons-e18ff9bb200a2eb092fb610d1592af76d420722d4d8b7d48d6b20c7911bf532a.svg#close"></use></svg>
<span class="collapse-text">Close sidebar</span>
</button>
<li class="hidden">
<a title="Activity" class="shortcuts-project-activity" href="/datadrivendiscovery/primitive-interfaces/activity"><span>
Activity
</span>
</a></li>
<li class="hidden">
<a title="Network" class="shortcuts-network" href="/datadrivendiscovery/primitive-interfaces/network/master">Graph
</a></li>
<li class="hidden">
<a title="Charts" class="shortcuts-repository-charts" href="/datadrivendiscovery/primitive-interfaces/graphs/master/charts">Charts
</a></li>
<li class="hidden">
<a class="shortcuts-new-issue" href="/datadrivendiscovery/primitive-interfaces/issues/new">Create a new issue
</a></li>
<li class="hidden">
<a title="Jobs" class="shortcuts-builds" href="/datadrivendiscovery/primitive-interfaces/-/jobs">Jobs
</a></li>
<li class="hidden">
<a title="Commits" class="shortcuts-commits" href="/datadrivendiscovery/primitive-interfaces/commits/master">Commits
</a></li>
<li class="hidden">
<a title="Issue Boards" class="shortcuts-issue-boards" href="/datadrivendiscovery/primitive-interfaces/boards">Issue Boards</a>
</li>
</ul>
</div>
</div>

<div class="content-wrapper page-with-new-nav">

<div class="mobile-overlay"></div>
<div class="alert-wrapper">




<nav class="breadcrumbs container-fluid container-limited" role="navigation">
<div class="breadcrumbs-container">
<button name="button" type="button" class="toggle-mobile-nav"><span class="sr-only">Open sidebar</span>
<i aria-hidden="true" data-hidden="true" class="fa fa-bars"></i>
</button><div class="breadcrumbs-links js-title-container">
<ul class="list-unstyled breadcrumbs-list js-breadcrumbs-list">
<li><a class="group-path breadcrumb-item-text js-breadcrumb-item-text " href="/datadrivendiscovery"><img class="avatar-tile lazy" width="15" height="15" data-src="https://assets.gitlab-static.net/uploads/-/system/group/avatar/2094972/d3m-onlight_3x.png" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" />datadrivendiscovery</a><svg class="s8 breadcrumbs-list-angle"><use xlink:href="https://gitlab.com/assets/icons-e18ff9bb200a2eb092fb610d1592af76d420722d4d8b7d48d6b20c7911bf532a.svg#angle-right"></use></svg></li> <li><a href="/datadrivendiscovery/primitive-interfaces"><span class="breadcrumb-item-text js-breadcrumb-item-text">primitive-interfaces</span></a><svg class="s8 breadcrumbs-list-angle"><use xlink:href="https://gitlab.com/assets/icons-e18ff9bb200a2eb092fb610d1592af76d420722d4d8b7d48d6b20c7911bf532a.svg#angle-right"></use></svg></li>

<li>
<h2 class="breadcrumbs-sub-title"><a href="/datadrivendiscovery/primitive-interfaces/blob/master/primitive_interfaces/base.py">Repository</a></h2>
</li>
</ul>
</div>

</div>
</nav>

<div class="flash-container flash-container-page">
</div>

</div>
<div class=" ">
<div class="content" id="content-body">

<div class="container-fluid container-limited">
<div class="tree-holder" id="tree-holder">
<div class="nav-block">
<div class="tree-ref-container">
<div class="tree-ref-holder">
<form class="project-refs-form" action="/datadrivendiscovery/primitive-interfaces/refs/switch" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="destination" id="destination" value="blob" />
<input type="hidden" name="path" id="path" value="primitive_interfaces/base.py" />
<div class="dropdown">
<button class="dropdown-menu-toggle js-project-refs-dropdown" type="button" data-toggle="dropdown" data-selected="master" data-ref="master" data-refs-url="/datadrivendiscovery/primitive-interfaces/refs?sort=updated_desc" data-field-name="ref" data-submit-form-on-click="true" data-visit="true"><span class="dropdown-toggle-text ">master</span><i aria-hidden="true" data-hidden="true" class="fa fa-chevron-down"></i></button>
<div class="dropdown-menu dropdown-menu-paging dropdown-menu-selectable git-revision-dropdown">
<div class="dropdown-page-one">
<div class="dropdown-title"><span>Switch branch/tag</span><button class="dropdown-title-button dropdown-menu-close" aria-label="Close" type="button"><i aria-hidden="true" data-hidden="true" class="fa fa-times dropdown-menu-close-icon"></i></button></div>
<div class="dropdown-input"><input type="search" id="" class="dropdown-input-field" placeholder="Search branches and tags" autocomplete="off" /><i aria-hidden="true" data-hidden="true" class="fa fa-search dropdown-input-search"></i><i role="button" aria-hidden="true" data-hidden="true" class="fa fa-times dropdown-input-clear js-dropdown-input-clear"></i></div>
<div class="dropdown-content"></div>
<div class="dropdown-loading"><i aria-hidden="true" data-hidden="true" class="fa fa-spinner fa-spin"></i></div>
</div>
</div>
</div>
</form>
</div>
<ul class="breadcrumb repo-breadcrumb">
<li>
<a href="/datadrivendiscovery/primitive-interfaces/tree/master">primitive-interfaces
</a></li>
<li>
<a href="/datadrivendiscovery/primitive-interfaces/tree/master/primitive_interfaces">primitive_interfaces</a>
</li>
<li>
<a href="/datadrivendiscovery/primitive-interfaces/blob/master/primitive_interfaces/base.py"><strong>base.py</strong>
</a></li>
</ul>
</div>
<div class="tree-controls">
<a class="btn shortcuts-find-file" rel="nofollow" href="/datadrivendiscovery/primitive-interfaces/find_file/master"><i aria-hidden="true" data-hidden="true" class="fa fa-search"></i>
<span>Find file</span>
</a>
<div class="btn-group" role="group"><a class="btn js-blob-blame-link" href="/datadrivendiscovery/primitive-interfaces/blame/master/primitive_interfaces/base.py">Blame</a><a class="btn" href="/datadrivendiscovery/primitive-interfaces/commits/master/primitive_interfaces/base.py">History</a><a class="btn js-data-file-blob-permalink-url" href="/datadrivendiscovery/primitive-interfaces/blob/14a40ffc06d9d56e4e8444446d8e194f044f7b4b/primitive_interfaces/base.py">Permalink</a></div>
</div>
</div>

<div class="info-well hidden-xs">
<div class="well-segment">
<ul class="blob-commit-info">
<li class="commit flex-row js-toggle-container" id="commit-ba5878eb">
<div class="avatar-cell hidden-xs">
<a href="/mitar"><img alt="Mitar&#39;s avatar" src="/uploads/-/system/user/avatar/706613/avatar.png" data-container="body" class="avatar s36 hidden-xs has-tooltip" title="Mitar" /></a>
</div>
<div class="commit-detail">
<div class="commit-content">
<a class="commit-row-message item-title" href="/datadrivendiscovery/primitive-interfaces/commit/ba5878ebc078cd2ddb4918232d0ccb08b0323b27">Improve base can_accept.</a>
<span class="commit-row-message visible-xs-inline">
&middot;
ba5878eb
</span>
<button class="text-expander hidden-xs js-toggle-button" type="button">...</button>
<pre class="commit-row-description js-toggle-content">&#x000A;Allow just types for non-pipeline arguments.</pre>
<div class="commiter">
<a class="commit-author-link has-tooltip" title="mitar.git@tnode.com" href="/mitar">Mitar</a> committed <time class="js-timeago" title="Dec 26, 2017 7:49pm" datetime="2017-12-26T19:49:20Z" data-toggle="tooltip" data-placement="bottom" data-container="body">Dec 26, 2017</time>
</div>
</div>
<div class="commit-actions flex-row hidden-xs">

<a class="commit-sha btn btn-transparent btn-link" href="/datadrivendiscovery/primitive-interfaces/commit/ba5878ebc078cd2ddb4918232d0ccb08b0323b27">ba5878eb</a>
<button class="btn btn-clipboard btn-transparent" data-toggle="tooltip" data-placement="bottom" data-container="body" data-title="Copy commit SHA to clipboard" data-clipboard-text="ba5878ebc078cd2ddb4918232d0ccb08b0323b27" type="button" title="Copy commit SHA to clipboard" aria-label="Copy commit SHA to clipboard"><i aria-hidden="true" aria-hidden="true" data-hidden="true" class="fa fa-clipboard"></i></button>

</div>
</div>
</li>

</ul>
</div>

</div>
<div class="blob-content-holder" id="blob-content-holder">
<article class="file-holder">
<div class="js-file-title file-title-flex-parent">
<div class="file-header-content">
<i aria-hidden="true" data-hidden="true" class="fa fa-file-text-o fa-fw"></i>
<strong class="file-title-name">
base.py
</strong>
<button class="btn btn-clipboard btn-transparent prepend-left-5" data-toggle="tooltip" data-placement="bottom" data-container="body" data-class="btn-clipboard btn-transparent prepend-left-5" data-title="Copy file path to clipboard" data-clipboard-text="{&quot;text&quot;:&quot;primitive_interfaces/base.py&quot;,&quot;gfm&quot;:&quot;`primitive_interfaces/base.py`&quot;}" type="button" title="Copy file path to clipboard" aria-label="Copy file path to clipboard"><i aria-hidden="true" aria-hidden="true" data-hidden="true" class="fa fa-clipboard"></i></button>
<small>
41.1 KB
</small>
</div>

<div class="file-actions">

<div class="btn-group" role="group"><button class="btn btn btn-sm js-copy-blob-source-btn" data-toggle="tooltip" data-placement="bottom" data-container="body" data-class="btn btn-sm js-copy-blob-source-btn" data-title="Copy source to clipboard" data-clipboard-target=".blob-content[data-blob-id=&#39;ce39a509b6a842baff84fd51eda96190939aff72&#39;]" type="button" title="Copy source to clipboard" aria-label="Copy source to clipboard"><i aria-hidden="true" aria-hidden="true" data-hidden="true" class="fa fa-clipboard"></i></button><a class="btn btn-sm has-tooltip" target="_blank" rel="noopener noreferrer" title="Open raw" data-container="body" href="/datadrivendiscovery/primitive-interfaces/raw/master/primitive_interfaces/base.py"><i aria-hidden="true" data-hidden="true" class="fa fa-file-code-o"></i></a></div>
<div class="btn-group" role="group"><span class="btn btn-sm path-lock disabled has-tooltip" data-toggle="tooltip" title="You do not have permission to lock this">Lock</span><button name="button" type="submit" class="btn js-edit-blob  js-edit-blob-link-fork-toggler" data-action="edit" data-fork-path="/datadrivendiscovery/primitive-interfaces/forks?continue%5Bnotice%5D=You%27re+not+allowed+to+make+changes+to+this+project+directly.+A+fork+of+this+project+has+been+created+that+you+can+make+changes+in%2C+so+you+can+submit+a+merge+request.&amp;continue%5Bnotice_now%5D=You%27re+not+allowed+to+make+changes+to+this+project+directly.+A+fork+of+this+project+is+being+created+that+you+can+make+changes+in%2C+so+you+can+submit+a+merge+request.&amp;continue%5Bto%5D=%2Fdatadrivendiscovery%2Fprimitive-interfaces%2Fedit%2Fmaster%2Fprimitive_interfaces%2Fbase.py&amp;namespace_key=2334978">Edit</button><button name="button" type="submit" class="btn btn-default js-edit-blob-link-fork-toggler" data-action="replace" data-fork-path="/datadrivendiscovery/primitive-interfaces/forks?continue%5Bnotice%5D=You%27re+not+allowed+to+make+changes+to+this+project+directly.+A+fork+of+this+project+has+been+created+that+you+can+make+changes+in%2C+so+you+can+submit+a+merge+request.+Try+to+replace+this+file+again.&amp;continue%5Bnotice_now%5D=You%27re+not+allowed+to+make+changes+to+this+project+directly.+A+fork+of+this+project+is+being+created+that+you+can+make+changes+in%2C+so+you+can+submit+a+merge+request.&amp;continue%5Bto%5D=%2Fdatadrivendiscovery%2Fprimitive-interfaces%2Fblob%2Fmaster%2Fprimitive_interfaces%2Fbase.py&amp;namespace_key=2334978">Replace</button><button name="button" type="submit" class="btn btn-remove js-edit-blob-link-fork-toggler" data-action="delete" data-fork-path="/datadrivendiscovery/primitive-interfaces/forks?continue%5Bnotice%5D=You%27re+not+allowed+to+make+changes+to+this+project+directly.+A+fork+of+this+project+has+been+created+that+you+can+make+changes+in%2C+so+you+can+submit+a+merge+request.+Try+to+delete+this+file+again.&amp;continue%5Bnotice_now%5D=You%27re+not+allowed+to+make+changes+to+this+project+directly.+A+fork+of+this+project+is+being+created+that+you+can+make+changes+in%2C+so+you+can+submit+a+merge+request.&amp;continue%5Bto%5D=%2Fdatadrivendiscovery%2Fprimitive-interfaces%2Fblob%2Fmaster%2Fprimitive_interfaces%2Fbase.py&amp;namespace_key=2334978">Delete</button></div>
</div>
</div>
<div class="js-file-fork-suggestion-section file-fork-suggestion hidden">
<span class="file-fork-suggestion-note">
You're not allowed to
<span class="js-file-fork-suggestion-section-action">
edit
</span>
files in this project directly. Please fork this project,
make your changes there, and submit a merge request.
</span>
<a class="js-fork-suggestion-button btn btn-grouped btn-inverted btn-new" rel="nofollow" data-method="post" href="/datadrivendiscovery/primitive-interfaces/blob/master/primitive_interfaces/base.py">Fork</a>
<button class="js-cancel-fork-suggestion-button btn btn-grouped" type="button">
Cancel
</button>
</div>

<script id="js-file-lock" type="application/json">
{"path":"primitive_interfaces/base.py","toggle_path":"/datadrivendiscovery/primitive-interfaces/path_locks/toggle"}
</script>

<div class="blob-viewer" data-type="simple" data-url="/datadrivendiscovery/primitive-interfaces/blob/master/primitive_interfaces/base.py?format=json&amp;viewer=simple">
<div class="text-center prepend-top-default append-bottom-default">
<i aria-hidden="true" aria-label="Loading content…" class="fa fa-spinner fa-spin fa-2x"></i>
</div>

</div>


</article>
</div>

</div>
</div>

</div>
</div>
</div>
</div>


</body>
</html>

