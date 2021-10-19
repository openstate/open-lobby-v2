<h1>Search</h1>
<p>Zoeken naar &quot;{params.query}&quot;</p>
<script>
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
