<template>
  <div id="app">
    <header>

      <NavBar /> 

    </header>
    <h1>{{ msg }}</h1>
    <p>
      A learning experience designed for junior developers to land and succeed in tech roles
    </p>

    <ul>

      <li><a href="www.aspiringblackcoders.com" target="_blank" rel="noopener">Log In Here</a></li>
    </ul>
    
  </div>
</template>

<script>

import NavBar from './NavBar'

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },

  components: {
    NavBar
   
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
