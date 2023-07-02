<template>
  <div class="hello">
    <header>
      <navbar /> 

    </header>
    <h1>{{ msg }}</h1>
    <p>
      A learning experience designed for junior developers to land and succeed in tech roles
    </p>
    <h3>Visit our community website!</h3>
    <ul>

      <li><a href="www.aspiringblackcoders.com" target="_blank" rel="noopener">Aspiring Black Coders</a></li>
    </ul>
    
  </div>
</template>

<script>

import navbar from './navbar'

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },

  components: {
    navbar
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
