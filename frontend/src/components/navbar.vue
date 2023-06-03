<template>
    <div>
        <nav class="navbar">
            <ul>
                <li><a href="#"> Home</a></li>
                <li><a href="#"> Course</a></li>
                <li><a href="#"> Progress</a></li>
            </ul>
        </nav>  
    </div>  
</template>


<script> 
    export default {
        name: 'NavBar'
    }
</script>


<style scoped> /* makes it so that only styling for navbar is here */

.navbar {
  background-color: #0b0a0a; /* Set the background color of the navbar */
  color: #fff; /* Set the text color to white */
  padding: 10px; /* Add some padding around the navbar */
  width: 100%; 
  position: absolute;
  top: 0; 
}

.navbar ul {
  list-style-type: none; /* Remove the default bullet points */
  margin: 0; /* Remove any default margin */
  padding: 0; /* Remove any default padding */
}

.navbar li {
  display: inline-block; /* Display the list items in a horizontal line */
  margin-right: 10px; /* Add some spacing between the list items */
}

.navbar a {
  color: #fff; /* Set the link color to white */
  text-decoration: none; /* Remove the underline from the links */
  padding: 5px; /* Add some padding around the links */
}

.navbar a:hover {
  background-color: #555; /* Change the background color on hover */
}

</style>