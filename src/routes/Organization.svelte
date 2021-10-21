{#if $main_obj}
  {#if $main_obj._source.memberships}
    {#each $main_obj._source.memberships as m}
      {#if m.organization_id == params.slug}
        <div class="odd-search-result">
        <Tile format="short" on:click={(e) => handleClick(e, main_obj)}>
          <Header>
            <Profile byline={m.organization.classification} type="business">
            { m.organization.name }
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
      {/if}
    {/each}
  {/if}
{/if}

<div class="tilerow-grid">
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
</div>

<script>
import { get } from 'svelte/store';

import {link, push} from 'svelte-spa-router';
import Button from '@soddk/button';
import Profile from '@soddk/common';
import Tile, {Header, Body, Actions, Action} from '@soddk/tile';

import { results, main_obj } from '../stores.js';
import { find_organization_with_members } from '../sources.js';
import { handleClick } from '../utils.js';

// You need to define the component prop "params"
export let params = {};
let first_org;

var groupBy = function(xs, key) {
  return xs.reduce(function(rv, x) {
    (rv[x[key]] = rv[x[key]] || []).push(x);
    return rv;
  }, {});
};

</script>

<script context="module">
export function perform_find_organization(org_slug) {
  console.log('executing organization search from module export');
  find_organization_with_members(org_slug);
}
</script>
