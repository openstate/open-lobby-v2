<h1 class="odd-header">Open Draaideur</h1>

<div class="odd-explanation">
<p>Wil jij ook weten waar onze politici terecht komen na hun ambtsperiode? Check het dan hier op Open Draaideur!</p>

<p>Lobbyen in Nederland is niet transparant en niet evenwichtig. Dat is niet goed voor het vertrouwen in politiek en democratie. Een belangrijk onderdeel van schimmige en onevenwichtige lobby is de ‘politieke draaideur’: politici (bewindspersonen, Kamerleden) komen na hun ambtsperiode weer terug in de politiek, maar nu als belangenbehartiger van een bedrijf, branche of specifieke groep.</p>
<p>Met deze tool schijnt <a href="http://openstate.eu" target="_blank">Open State Foundation</a> licht op de politieke draaideur. Zoek en vergelijk zelf waar politici die de afgelopen tien jaar zijn vertrokken, naartoe zijn gegaan. Zoek op naam, partij, bedrijf of organisatie.</p>
<Searchbar />
</div>

<script>
import {link, push} from 'svelte-spa-router';
import Button from '@soddk/button';
import Profile from '@soddk/common';
import Tile, {Header, Body, Actions, Action} from '@soddk/tile';
import Searchbar from './Searchbar.svelte';

import { search_request } from '../sources.js';
</script>

<style>
</style>
