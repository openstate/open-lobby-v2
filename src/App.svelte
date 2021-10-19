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
import NotFound from './routes/NotFound.svelte';

// import Author from './routes/Author.svelte'
// import Book from './routes/Book.svelte'
// import NotFound from './routes/NotFound.svelte'
const routes = {
    // Exact path
    '/': Home,
    '/over': About,
    '/zoeken/:query': Search,
    '/p/:slug': Person,
    '/o/:slug': Organization,
    '*': NotFound,
}
</script>
<svelte:head>
  <title>Open Draaideur</title>
</svelte:head>

<body>
  <div class="app-container">
    <Workspace>
      <Menubar>
        <Logo/>
        <MenuItems>
        <MenuItem href="/data">Data</MenuItem>
          <MenuItem href="#/over">Over</MenuItem>
        </MenuItems>
      </Menubar>

      <div class="contents">
        <Router {routes}/>
      </div>
    </Workspace>
  </div>
</body>
