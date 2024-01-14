
<template>
<div>
  <nav id="app">
      <ul>
       <router-link to="/HomePage">Home</router-link>
       <router-link to="/LearnPage">Learn</router-link>
      <router-link to="/YourProfile">YourProfile</router-link>
      </ul>
      <router-view></router-view>
  </nav>

    
  </div>

</template>


<script> 
    export default {
        name: 'NavBar'
    };

</script>


<style scoped> /* makes it so that only styling for navbar is here */

#app {
  background-color: #0b0a0a; /* Set the background color of the navbar */
  color: #fff; /* Set the text color to white */
  padding: 10px; /* Add some padding around the navbar */
  width: 100%; 
  position: absolute;
  top: 0; 
}

#app {
  list-style-type: none; /* Remove the default bullet points */
  margin: 0; /* Remove any default margin */
  padding: 0; /* Remove any default padding */
}

#app li {
  display: inline-block; /* Display the list items in a horizontal line */
  margin-right: 10px; /* Add some spacing between the list items */
}

#app a {
  color: #fff; /* Set the link color to white */
  text-decoration: none; /* Remove the underline from the links */
  padding: 5px; /* Add some padding around the links */
}

#app a:hover {
  background-color: #555; /* Change the background color on hover */
}

</style>