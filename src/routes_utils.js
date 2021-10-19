import { search_request } from './sources.js';

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
        search_request(event.detail.params.query);
    }
}
