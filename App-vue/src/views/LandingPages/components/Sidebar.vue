<!-- Sidebar.vue -->
<template>
    <div class="sidebar">
      <!-- En-tête du sidebar avec logo -->
      <div class="sidebar-header">
        <img src="/src/assets/img/logo-removebg-preview.png" alt="Logo" class="company-logo"/>
        <h1 class="company-name">TechTalent</h1>
      </div>
  
      <!-- Menu principal -->
      <nav class="sidebar-nav">
        <ul class="nav-list">
          <li class="nav-item">
            <router-link to="/dashboard" class="nav-link" active-class="active">
              <i class="fas fa-home"></i>
              <span>Dashboard</span>
            </router-link>
          </li>
          
       
          <li class="nav-item">
            <router-link to="/company/edit-profile" class="nav-link" active-class="active">
              <i class="fas fa-calendar"></i>
              <span>Modéfier le profile</span>
            </router-link>
          </li>

          <li class="nav-item">
            <router-link to="/" class="nav-link" active-class="active">
              <i class="fas fa-calendar"></i>
              <span>Logout</span>
            </router-link>
          </li>
        </ul>
      </nav>
  
      <!-- Profile section en bas -->
      <div class="sidebar-profile">
        <div class="profile-info">
          <router-link to="/company/profile" class="profile-info">
          <img src="/src/assets/img/logo1.jpg" alt="Profile" class="profile-image"/>
          <div class="profile-details">
            <p class="profile-name">John Doe</p>
            <p class="profile-role">Recruteur</p>
          </div>
        </router-link>
        </div>
        <button class="profile-edit-btn">
          <i class="fas fa-cog"></i>
        </button>
      </div>
    </div>
  </template>
  
  <script setup>
  // Vous pouvez ajouter ici la logique nécessaire
  </script>
  
  <style scoped>
  .sidebar {
    width: 260px;
    height: 100vh;
    background-color: #1b1b1f;
    color: white;
    display: flex;
    flex-direction: column;
    position: fixed;
    left: 0;
    top: 0;
  }
  
  .sidebar-header {
    padding: 1.5rem;
    display: flex;
    align-items: center;
    gap: 1rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  }
  
  .company-logo {
    width: 40px;
    height: 40px;
    object-fit: cover;
    border-radius: 8px;
  }
  
  .company-name {
    font-size: 1.2rem;
    font-weight: 600;
    color: rgb(247, 244, 244);
  }
  
  .sidebar-nav {
    flex: 1;
    padding: 1.5rem 0;
  }
  
  .nav-list {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  
  .nav-item {
    margin: 0.5rem 0;
  }
  
  .nav-link {
    display: flex;
    align-items: center;
    padding: 0.75rem 1.5rem;
    color: rgba(255, 255, 255, 0.7);
    text-decoration: none;
    transition: all 0.3s;
    gap: 1rem;
  }
  
  .nav-link:hover, .nav-link.active {
    background-color: rgba(255, 255, 255, 0.1);
    color: white;
  }
  
  .nav-link i {
    width: 20px;
  }
  
  .sidebar-profile {
    padding: 1.5rem;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  
  .profile-info {
    display: flex;
    align-items: center;
    gap: 1rem;
    text-decoration: none;
  color: inherit;
  }
  .profile-info:hover {
  opacity: 0.9;
}
  
  .profile-image {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    object-fit: cover;
  }
  
  .profile-name {
    font-weight: 600;
    margin: 0;
  }
  
  .profile-role {
    font-size: 0.875rem;
    color: rgba(255, 255, 255, 0.7);
    margin: 0;
  }
  
  .profile-edit-btn {
    background: none;
    border: none;
    color: rgba(255, 255, 255, 0.7);
    cursor: pointer;
    padding: 0.5rem;
    border-radius: 50%;
    transition: all 0.3s;
  }
  
  .profile-edit-btn:hover {
    background-color: rgba(255, 255, 255, 0.1);
    color: white;
  }
  </style>