<h1>About</h1>
<p>This is the about page.</p>
<script>
import {link, push} from 'svelte-spa-router';
import Button from '@soddk/button';
import Profile from '@soddk/common';
import Tile, {Header, Body, Actions, Action} from '@soddk/tile';

import { results } from '../stores.js';
import { find_organization_with_members } from '../sources.js';
// You need to define the component prop "params"
export let params = {};

function handleClick(e, r) {
  e.preventDefault();
		console.log('Button Clicked for ', r._source.id);
    return false;
	}
</script>

<script context="module">
export function perform_find_organization(org_slug) {
  console.log('executing search from module export');
  find_organization_with_members(org_slug);
}
</script>
