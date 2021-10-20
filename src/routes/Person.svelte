{#each $results as r}
<div class="odd-search-result">
<Tile format="short" on:click={(e) => handleClick(e, r)}>
  <Header>
    <Profile>
    { r._source.name }
    </Profile>
  </Header>
  <Body>
  <!--
  <Body image="https://via.placeholder.com/250x170">
  <h3>Titel van Artikel</h3> -->
  { r._source.description }
  </Body>
  <!--
  <Actions>
    <Action on:click={handleClick}>Deel op Twitter</Action>
    <Action on:click={handleClick}>Deel op Facebook</Action>
  </Actions> -->
</Tile>
</div>
{/each}

<script>
import {link, push} from 'svelte-spa-router';
import Button from '@soddk/button';
import Profile from '@soddk/common';
import Tile, {Header, Body, Actions, Action} from '@soddk/tile';

import { results } from '../stores.js';
import { find_person } from '../sources.js';
// You need to define the component prop "params"
export let params = {};

function handleClick(e, r) {
  e.preventDefault();
		console.log('Button Clicked for ', r._source.id);
    return false;
	}
</script>

<script context="module">
export function perform_find_person(per_slug) {
  console.log('executing search from module export');
  find_person(per_slug);
}
</script>
