<svelte:head>
  <title>Open Lobby</title>
</svelte:head>

<div class="app-container">
<Workspace>
<Menubar>
  <Logo/>
  <MenuItems>
  <MenuItem href="/data">Data</MenuItem>
    <MenuItem href="#/over">Over</MenuItem>
  </MenuItems>
</Menubar>
<h1>OpenDraaideur</h1>
<div class="tilerow">
  <Tile format="short">
    <Header>
      <Profile byline="Developer">
      Breyten Ernsting
      </Profile>
    </Header>
    <Body image="https://via.placeholder.com/250x170">
    <h3>Titel van Artikel</h3>
    Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum
    </Body>
    <Actions>
      <Action on:click={handleClick}>Deel op Twitter</Action>
      <Action on:click={handleClick}>Deel op Facebook</Action>
    </Actions>
  </Tile>

  <Tile format="short">
    <Header>
      <Profile byline="Developer">
      Breyten Ernsting
      </Profile>
      <div>
      <Button variant="normal" on:click={handleClick}>Bron</Button>
      </div>
    </Header>
    <Body image="https://via.placeholder.com/250x170">
    <h3>Titel van Artikel</h3>
    Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum
    </Body>
    <Actions>
      <Action on:click={handleClick}>Deel op Twitter</Action>
      <Action on:click={handleClick}>Deel op Facebook</Action>
    </Actions>
  </Tile>

</div>
<div>
<Profile on:click={handleClick}>
Breyten Ernsting
</Profile>
</div>
<div>
</div>
<p><a href="/over" use:link>Over pagina</a></p>
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
import {link} from 'svelte-spa-router';
import Workspace from '@soddk/workspace';
import Menubar, {Logo, MenuItems, MenuItem} from '@soddk/menubar';
import Button from '@soddk/button';
import Profile from '@soddk/common';
import Tile, {Header, Body, Actions, Action} from '@soddk/tile';

function handleClick(e) {
  e.preventDefault();
		alert('Button Clicked');
    return false;
	}
</script>

<style>
</style>
