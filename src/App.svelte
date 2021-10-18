<script>
import Router from 'svelte-spa-router';

import {link} from 'svelte-spa-router';
import Workspace from '@soddk/workspace';
import Menubar, {Logo, MenuItems, MenuItem} from '@soddk/menubar';

import Home from './routes/Home.svelte';
import About from './routes/About.svelte';
// import Author from './routes/Author.svelte'
// import Book from './routes/Book.svelte'
// import NotFound from './routes/NotFound.svelte'
const routes = {
    // Exact path
    '/': Home,
    '/over': About
    // Using named parameters, with last being optional
    //'/author/:first/:last?': Author,

    // Wildcard parameter
    //'/book/*': Book,

    // Catch-all
    // This is optional, but if present it must be the last
    //'*': NotFound,
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
