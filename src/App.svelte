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
<div>
<Profile on:click={handleClick}>
Breyten Ernsting
</Profile>
</div>
<div>
<Profile byline="Developer">
Breyten Ernsting
</Profile>
</div>
<p><a href="#" on:click={handleClick}>Testing123</p>
<div>
<Button href="/" on:click={handleClick} title="Test">Zoeken</Button>
</div>
<div>
<Button variant="cta" on:click={handleClick}>Zoeken</Button>
</div>
<div>
<Button variant="raised" on:click={handleClick}>Zoeken</Button>
</div>
</Workspace>
</div>

<script>
import Workspace from '@soddk/workspace';
import Menubar, {Logo, MenuItems, MenuItem} from '@soddk/menubar';
import Button from '@soddk/button';
import Profile from '@soddk/common';

function handleClick(e) {
  e.preventDefault();
		alert('Button Clicked');
    return false;
	}
</script>

<style>
</style>
