import { search_request } from './sources.js';

import { perform_search } from './routes/Search.svelte';
import { perform_find_person } from './routes/Person.svelte';
import { perform_find_organization } from './routes/Organization.svelte';

export function routeLoading(event) {
    console.log('routeLoading event')
    console.log('Route', event.detail.route)
    console.log('Location', event.detail.location)
    console.log('Querystring', event.detail.querystring)
    console.log('User data', event.detail.userData)
}

export function routeLoaded(event) {
    console.log('routeLoaded event')
    // The first 5 properties are the same as for the routeLoading event
    console.log('Route', event.detail.route)
    console.log('Location', event.detail.location)
    console.log('Querystring', event.detail.querystring)
    console.log('Params', event.detail.params)
    console.log('User data', event.detail.userData)
    // The last two properties are unique to routeLoaded
    console.log('Component', event.detail.component) // This is a Svelte component, so a function
    console.log('Name', event.detail.name)

    if (event.detail.name == 'Search') {
        perform_search(event.detail.params.query);
    }
    if (event.detail.name == 'Person') {
      perform_find_person(event.detail.params.slug);
    }
    if (event.detail.name == 'Organization') {
      perform_find_organization(event.detail.params.slug);
    }
}
