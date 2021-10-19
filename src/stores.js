import { readable, writable, get, derived } from 'svelte/store';
import { onMount } from "svelte";

let results = writable([]);
