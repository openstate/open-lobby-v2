import { readable, writable, get, derived } from 'svelte/store';
import { onMount } from "svelte";

export let results = writable([]);
export let total_results = writable(0);
export let main_obj = writable(null);
