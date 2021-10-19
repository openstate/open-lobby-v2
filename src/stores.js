import { readable, writable, get, derived } from 'svelte/store';
import { onMount } from "svelte";

export let results = writable([]);
