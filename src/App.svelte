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
<div>
<Button href="/" on:click={() => console.log('clicked!')}>Zoeken</Button>
</div>
<div>
<Button variant="cta">Zoeken</Button>
</div>
<div>
<Button variant="raised">Zoeken</Button>
</div>
</Workspace>
</div>

<script>
import Workspace from '@soddk/workspace';
import Menubar, {Logo, MenuItems, MenuItem} from '@soddk/menubar';
import Button from '@soddk/button';
</script>

<style>
</style>
