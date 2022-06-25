<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p>
      A learning experience designed for junior developers to land and succeed in tech roles
      <a href="https://cli.vuejs.org" target="_blank" rel="noopener">vue-cli documentation</a>.
    </p>
    <h3>Visit our community website!</h3>
    <ul>
      <li><a href="www.aspiringblackcoders.com" target="_blank" rel="noopener">babel</a></li>
    </ul>
    
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
