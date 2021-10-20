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
        results.set(data.hits.hits);
      });
}

export function search_request(query) {
  // http://api.opendraaideur.nl/search?query=rutte
  return api_request({
    query: query,
    limit: 1000
  });
}

export function find_person(per_slug) {
  // http://api.opendraaideur.nl/persons/search?filter=id.keyword:mark-rutte
  return api_request('persons', {
    filter: "id.keyword:" + per_slug,
    limit: 1000
  });
}

export function find_organization(org_slug) {
  // http://api.opendraaideur.nl/organizations/search?filter=id.keyword:vvd
  return api_request('organizations', {
    filter: "id.keyword:" + per_slug,
    limit: 1000
  });
}

export function find_organization_with_members(org_slug) {
  //  http://api.opendraaideur.nl/persons/search?filter=memberships.organization.id.keyword:vvd
  return api_request('persons', {
    filter: "memberships.organization.id.keyword:" + org_slug,
    limit: 1000
  });
}
