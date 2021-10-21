<p style="text-align: center;">Zoeken naar &quot;{params.query}&quot; leverde {$total_results} resultaten op.</p>

{#each $results as r}
<div class="odd-search-result">
<Tile format="short" on:click={(e) => handleClick(e, r)}>
  <Header>
    {#if is_person(r)}
    <Profile type="person">
    { r._source.name }
    </Profile>
    {:else}
    <Profile type="business">
    { r._source.name }
    </Profile>
    {/if}
  </Header>
  <Body>
  <!--
  <Body image="https://via.placeholder.com/250x170">
  <h3>Titel van Artikel</h3> -->
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

import { is_person, is_organization, handleClick } from '../utils.js';
import { results, total_results } from '../stores.js';
import { search_request } from '../sources.js';
// You need to define the component prop "params"
export let params = {};

</script>

<script context="module">
export function perform_search(query) {
  console.log('executing search from module export');
  search_request(query);
}
</script>
