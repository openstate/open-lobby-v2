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
    </Body>
    <!--
    <Actions>
      <Action on:click={handleClick}>Deel op Twitter</Action>
      <Action on:click={handleClick}>Deel op Facebook</Action>
    </Actions> -->
  </Tile>
  </div>

  {#if r._source.memberships}
  <code><pre>
  { JSON.stringify(r, null, 2) }
  </pre></code>

  {#each groupMemberships(r._source.sorted_memberships) as [k,v]}
    <p>{k}: {v}</p>
  {/each}
  {#each r._source.memberships.reverse() as m}
    {#if m.start_date}
      <div class="odd-bar"> </div>
      {#if m.start_date.endsWith('-01-01')}
      <div class="odd-year">{m.start_date.slice(0,4)}</div>
      {:else}
      <div class="odd-year">{m.start_date}</div>
      {/if}
    {/if}
    <div class="odd-bar"> </div>
    <div class="odd-search-result">
    <Tile format="short" on:click={(e) => handleClick(e, r)}>
      <Header>
        <Profile byline="{m.organization.classification}">
        { m .organization.name }
        </Profile>
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
  {/if}

  {#if r._source.description}
  <div class="odd-year">Nevenfuncties</div>

  <div class="odd-search-result">
  <Tile format="short">
    <Body>
    <!--
    <Body image="https://via.placeholder.com/250x170">
    <h3>Titel van Artikel</h3> -->
    { r._source.description }
    </Body>
  </Tile>
  </div>
  {/if}
{/each}

<script>
import {link, push} from 'svelte-spa-router';
import Button from '@soddk/button';
import Profile from '@soddk/common';
import Tile, {Header, Body, Actions, Action} from '@soddk/tile';

import { results } from '../stores.js';
import { find_person } from '../sources.js';
import { handleClick } from '../utils.js';

// You need to define the component prop "params"
export let params = {};

function groupMemberships(memberships) {
  var membership_entries = Object.entries(memberships);
  membership_entries.sort(sortYears);
  return membership_entries.reverse();
}

function sortYears(a, b) {
  var ya = a[0];
  var oa = a[1];
  var yb = b[0];
  var ob = b[1];
  if (ya == 'undefined') {
    return -1;
  }
  if (yb == 'undefined') {
    return 1;
  }
  if (ya == yb) {
    return 0;
  }
  if (ya > yb) {
    return 1;
  } else {
    return -1;
  }
}
</script>

<script context="module">

export function perform_find_person(per_slug) {
  console.log('executing person search from module export');
  find_person(per_slug);
}
</script>
