let root = 'https://cnodejs.org/api/v1'
let request = require('superagent')

function toType (obj) {
  return ({}).toString.call(obj).match(/\s([a-zA-Z]+)/)[1].toLowerCase()
}

function filterNull (o) {
  for (var key in o) {
    if (o[key] == null) {
      delete o[key]
    }
    if (toType(o[key]) === 'string') {
      o[key] = o[key].trim()
      if (o[key].length === 0) {
        delete o[key]
      }
    }
  }
  return o
}

function _apiBase (method, url, params, success, failure) {
  let r = request(method, url).type('text/plain')
  if (params) {
    params = filterNull(params)
    if (method === 'POST' || method === 'PUT') {
      if (toType(params) === 'object') {
        params = JSON.stringify(params)
      }
      r = r.send(params)
    } else if (method === 'GET' || method === 'DELETE') {
      r = r.query(params)
    }
  }
  r.end(function (err, res) {
    if (err) {
      alert('api error, HTTP CODE: ' + res.status)
      return
    };
    if (res.body.success === true) {
      if (success) {
        success(res.body)
      }
    } else {
      if (failure) {
        failure(res.body)
      } else {
        alert('error: ' + JSON.stringify(res.body))
      }
    }
  })
}

export default {
  get: function (url, params, success, failure) {
    return _apiBase('GET', root + '/' + url, params, success, failure)
  },
  post: function (url, params, success, failure) {
    return _apiBase('POST', root + '/' + url, params, success, failure)
  },
  put: function (url, params, success, failure) {
    return _apiBase('PUT', root + '/' + url, params, success, failure)
  },
  delete: function (url, params, success, failure) {
    return _apiBase('DELETE', root + '/' + url, params, success, failure)
  }
}
