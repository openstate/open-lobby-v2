import { get } from 'svelte/store';
import { results, total_results, main_obj } from './stores.js';

var groupBy = function(xs, key, fnc) {
  return xs.reduce(function(rv, x) {
    var rkey = (typeof(fnc) === 'undefined') ? x[key] : fnc(x[key]);
    (rv[rkey] = rv[rkey] || []).push(x);
    return rv;
  }, {});
};

var getYear = function(sdate) {
  if (sdate) {
    return sdate.slice(0,4);
  }
}

function api_request(params, index) {
  var url = window.location.protocol + '//api.opendraaideur.nl';
  if (typeof(index) !== 'undefined') {
    url += '/' + index;
  }
  url += '/search?' + new URLSearchParams(params).toString();
  return fetch(
    url, {}).then(
      response => response.json()
    ).then(
      function (data) {
        console.log('got data:');
        console.dir(data);
        if (data.hits.total.value > 0) {
          console.log('Setting main object to:', data.hits.hits[0]);
          main_obj.set(data.hits.hits[0]);
        } else {
          main_obj.set(null);
        }
        results.set(data.hits.hits.map(function (i) {
          if (typeof(i._source.memberships) !== 'undefined') {
            i._source.sorted_memberships = groupBy(i._source.memberships, 'start_date', getYear);
          }
          return i;
        }));
        total_results.set(data.hits.total.value || 0);
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
  return api_request({
    filter: "id.keyword:" + per_slug,
    limit: 1000
  }, 'persons');
}

export function find_organization(org_slug) {
  // http://api.opendraaideur.nl/organizations/search?filter=id.keyword:vvd
  return api_request({
    filter: "id.keyword:" + per_slug,
    limit: 1000
  }, 'organizations');
}

export function find_organization_with_members(org_slug) {
  //  http://api.opendraaideur.nl/persons/search?filter=memberships.organization.id.keyword:vvd
  return api_request({
    filter: "memberships.organization.id.keyword:" + org_slug,
    limit: 1000
  }, 'persons');
}
