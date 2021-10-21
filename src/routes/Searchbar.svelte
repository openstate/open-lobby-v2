<div class="odd-home">
  <form class="odd-search-form">
    <input type="text" name="query" placeholder="Rutte, SP, KLM..." bind:value={query} on:change={handleSearch}>
    <input type="submit" value="Zoeken" class="oddk-button oddk-button-raised" on:click={handleSearch}>
  </form>
</div>
<script>
import {link, push} from 'svelte-spa-router';

export let query;

function handleClick(e) {
  e.preventDefault();
		alert('Button Clicked');
    return false;
	}


function handleSearch(e) {
  e.preventDefault();
  //alert('Should go and search for "' + query + '" now!');
  push('/zoeken/' + encodeURIComponent(query));
  return false;
}
</script>
