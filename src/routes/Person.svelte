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
  { JSON.stringify(groupBy(r._source.memberships, 'start_date', getYear), null, 2) }
  </pre></code>

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

var getYear = function(sdate) {
  if (sdate) {
    return sdate.slice(0,4);
  }
}
</script>

<script context="module">

var groupBy = function(xs, key, fnc) {
  return xs.reduce(function(rv, x) {
    var rkey = (typeof(fnc) === 'undefined') ? x[key] : fnc(x[key]);
    (rv[rkey] = rv[rkey] || []).push(x);
    return rv;
  }, {});
};

export function perform_find_person(per_slug) {
  console.log('executing person search from module export');
  find_person(per_slug);
}
</script>
