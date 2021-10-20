export function is_person(result) {
  return result._index.endsWith('_persons');
}

export function is_organization(result) {
  return result._index.endsWith('_organizations');
}
