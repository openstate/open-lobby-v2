<script>
import Router from 'svelte-spa-router';

import {link} from 'svelte-spa-router';
import Workspace from '@soddk/workspace';
import Menubar, {Logo, MenuItems, MenuItem} from '@soddk/menubar';

import Home from './routes/Home.svelte';
import About from './routes/About.svelte';
import Person from './routes/Person.svelte';
import Organization from './routes/Organization.svelte';
import Search from './routes/Search.svelte';
import Analysis from './routes/Analysis.svelte';
import NotFound from './routes/NotFound.svelte';

import { routeLoading, routeLoaded } from './routes_utils.js';
// import Author from './routes/Author.svelte'
// import Book from './routes/Book.svelte'
// import NotFound from './routes/NotFound.svelte'
const routes = {
    // Exact path
    '/': Home,
    '/over': About,
    '/analyse': Analysis,
    '/zoeken/:query': Search,
    '/p/:slug': Person,
    '/o/:slug': Organization,
    '*': NotFound,
}
</script>
<svelte:head>
  <title>Open Draaideur</title>
  <meta name="twitter:card" content="summary">
  <meta property="og:image" content="https://openstate.eu/wp-content/themes/open-state-theme/dist/images/logo-open-state-foundation-og.png">
  <meta property="og:title" content="Open Draaideur">
  <meta property="og:description" content="Wil jij ook weten waar onze politici terecht komen na hun ambtsperiode? Check het dan hier!">
</svelte:head>

<body>
  <div class="app-container">
    <Workspace>
      <Menubar>
        <Logo/>
        <MenuItems>
        <MenuItem href="#/analyse">Analyse</MenuItem>
          <MenuItem href="#/over">Over</MenuItem>
        </MenuItems>
      </Menubar>

      <div class="contents">
        <Router {routes} on:routeLoading={routeLoading} on:routeLoaded={routeLoaded} />
      </div>
    </Workspace>
  </div>
</body>
