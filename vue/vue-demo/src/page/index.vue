<template>
  <div>
    <h1 class="logo">cnodejs Api Test</h1>
    <ul class="list">
      <li v-for="item in lists" v-text="item.title"></li>
    </ul>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        lists: []
      }
    },
    created () {
      this.get_data()
    },
    methods: {
      get_data: function (params) {
        if (!params) {
          params = {}
        }
        this.$api.get('topics', params, r => {
          this.lists = r.data
          console.log(r)
        })
      }
    }
  }
</script>
