<svelte:head>
  <title>Open Lobby</title>
</svelte:head>

<div class="app-container">
<Workspace>
<Menubar>
  <Logo/>
  <MenuItems>
  <MenuItem href="/data">Data</MenuItem>
    <MenuItem href="/over">Over</MenuItem>
  </MenuItems>
</Menubar>
<h1>OpenDraaideur</h1>
<p>Testing123</p>
</Workspace>
</div>

<script>
import Workspace from '@soddk/workspace';
import Menubar, {Logo, MenuItems, MenuItem} from '@soddk/menubar';
</script>

<style>
</style>
