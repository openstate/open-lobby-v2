import { get } from 'svelte/store';
import { results } from './stores.js';

function api_request(params, index) {
  var url = window.location.protocol + '//api.opendraaideur.nl';
  if (typeof(index) !== 'undefined') {
    url += index;
  }
  url += '/search?' + new URLSearchParams(params).toString();
  return fetch(
    url, {}).then(
      response => response.json()
    ).then(
      function (data) {
        console.log('got data:');
        console.dir(data);
        results.set(data);
      });
}

export function search_request(query) {
  return api_request({
    query: query,
    limit: 1000
  });
}
