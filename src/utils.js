import {link, push} from 'svelte-spa-router';


export function is_person(result) {
  return result._index.endsWith('_persons');
}

export function is_organization(result) {
  return result._index.endsWith('_organizations');
}

export function handleClick(e, r) {
  e.preventDefault();
	console.log('Button Clicked for ', r._source.id);
  if (is_person(r)) {
    push('/p/' + r._source.id);
  } else if (is_organization(r)) {
    push('/o/' + r._source.id);
  }
  return false;
}
