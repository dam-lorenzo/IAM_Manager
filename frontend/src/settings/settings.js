const home = '/'
const managment = '/managment'
const users_table = '/users'
const services_table = '/services'
const roles_table = '/roles'
const api_base_url = process.env.REACT_APP_API_URL
const api_base_storage = api_base_url + '/storage'
const api_search = api_base_storage + '/search'
const api_search_users = api_search + users_table
const api_seach_services = api_search + services_table
const api_search_roles = api_search + roles_table

export { home, managment, api_search_users }