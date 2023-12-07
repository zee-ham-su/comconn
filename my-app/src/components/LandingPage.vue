<template>
<div class="feature2">
    <img src="../assets/feature2_img.png" alt="feature img" class="img3">
    <div class="text-box2">
    <h2>Community Reviews</h2>
    <p>With the help of the reviews left by other users about the critical resources in your commmunity, 
      you are going to be up-to-date with about the critical resources so you are not left stranded. 
      You can also add you reviews to help and also help improve the facilities you visited</p>
    </div>
</div>
<div class="feature2">
    <div class="text-box3">
    <h2>About Our Project</h2>
    <p>The genesis of this project was a genuine desire to address a prevalent challenge—restricted 
        access to accurate and up-to-date information about critical community resources. 
        The inspiration struck as I observed the difficulties people faced in obtaining essential 
        information about their communities. This personal experience fueled a passion to create 
        a solution that would empower individuals with the right resources at their fingertips.
    </p>

    <p>The journey began with ideation and planning, shaping the vision into a tangible project. 
        The development process spanned several weeks, involving meticulous design, backend 
        implementation, and now, the frontend aspects. Each phase brought its own set of challenges
        and triumphs, contributing to a comprehensive and robust solution.
    </p>

    <P>
        This project is not merely a technical endeavor; it's a Portfolio Project for 
        Holberton School. It represents the culmination of theoretical knowledge and 
        hands-on application gained throughout the course. As a student at Holberton, 
        this undertaking showcases the skills acquired in web development, 
        user authentication, and integration of dynamic features.
    </P>
    </div>
</div>
<div>
    <div  class="text-box3">
    <h3>Meet the Team</h3>

    <ul>
      <li>
        <strong>Team Member 1:</strong>
        <a :href="linkedinLink1" target="_blank">LinkedIn</a>,
        <a :href="githubLink1" target="_blank">GitHub</a>,
        <a :href="twitterLink1" target="_blank">Twitter</a>
      </li>
      <!-- Repeat the above structure for each team member -->
    </ul>

    <h3>GitHub Repository</h3>
    <p>
      Explore the codebase on our
      <a :href="githubRepoLink" target="_blank">GitHub repository</a>.
    </p>
    </div>
</div>
</template>

<style scoped>
.img3{
  /*display: flex;
  position: relative;
  right: auto;*/
  float: right;
  width: 54%;
  margin: 20px;
}
.text-box2{
    margin-left: 20px;
    padding: 20px;
  }

.text-box3{
    margin-top: 350px;
    text-align: center;
    }
</style>