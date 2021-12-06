<h1 class="odd-header">Open Draaideur</h1>

<div class="odd-explanation">
<p>Wil jij ook weten waar onze politici terecht komen na hun ambtsperiode? Check het dan hier op Open Draaideur!</p>

<p>Lobbyen in Nederland is niet transparant en niet evenwichtig. Dat is niet goed voor het vertrouwen in politiek en democratie. Een belangrijk onderdeel van schimmige en onevenwichtige lobby is de ‘politieke draaideur’: politici (bewindspersonen, Kamerleden) komen na hun ambtsperiode weer terug in de politiek, maar nu als belangenbehartiger van een bedrijf, branche of specifieke groep.</p>
<p>Met deze tool schijnt <a href="http://openstate.eu" target="_blank">Open State Foundation</a> licht op de politieke draaideur. Zoek en vergelijk zelf waar politici die de afgelopen tien jaar zijn vertrokken, naartoe zijn gegaan. Zoek op naam, partij, bedrijf of organisatie.</p>
<Searchbar />
</div>

<div>
  <H1>H1 Header 1</H1>
</div>

<div>
  <H2>H2 Header 2</H2>
  <H2 variant="alt">H2 Header 2</H2>
</div>

<div>
  <Tag>Tag</Tag>
</div>

<div>
  <Tag variant="big">Grote tag</Tag>
</div>
<div>
  <IconButton>
    <Fa icon={faPen} size="1.20x" />
  </IconButton>
  <IconButton>
    <Fa icon={faArrowUp} size="1.20x" />
  </IconButton>
  <IconButton>
    <Fa icon={faArrowDown} size="1.20x" />
  </IconButton>
  <IconButton>
    <Fa icon={faChevronLeft} size="1.20x" />
  </IconButton>
  <IconButton>
    <Fa icon={faChevronRight} size="1.20x" />
  </IconButton>
</div>
<div>
  <IconButton>
    <Fa icon={faSignOutAlt} size="1.20x" />
  </IconButton>
  <IconButton>
    <Fa icon={faCog} size="1.20x" />
  </IconButton>
</div>

<div>
<h1>Font-awesome</h1>
Notification :
<Fa icon={faFlag} size="lg" /> Flag


<i class='fas fa-bell' style='font-size:24px'></i>
<br><br>
Message or Inbox :
<i class='fas fa-envelope' style='font-size:24px'></i>
<br><br>
Bookmark :
<i class='fas fa-bookmark' style='font-size:24px'></i>
<br><br>
Like Button :
<i class='fas fa-thumbs-up' style='font-size:24px'></i>
<br><br>
Calendar:
<i class='fas fa-calendar-alt' style='font-size:24px'></i>
</div>
<script>
import Fa from 'svelte-fa';
import { faFlag, faPen, faArrowUp, faArrowDown, faChevronRight, faChevronLeft, faSignOutAlt, faCog } from '@fortawesome/free-solid-svg-icons';
import {link, push} from 'svelte-spa-router';
import Button from '@soddk/button';
import Profile, {H1, H2, Tag} from '@soddk/common';
import Tile, {Header, Body, Actions, Action} from '@soddk/tile';
import Searchbar from './Searchbar.svelte';
import IconButton from '@soddk/icon-button';
import { search_request } from '../sources.js';
</script>

<style>
</style>
