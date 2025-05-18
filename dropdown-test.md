---
layout: default
title: Dropdown Test
---

<style>
  /* Simplified styles for testing */
  .test-navbar {
    background-color: #333;
    padding: 10px;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
  }
  
  .test-logo {
    color: white;
    font-weight: bold;
    margin-right: 20px;
  }
  
  .test-nav {
    position: relative;
  }
  
  .test-button {
    background-color: #444;
    color: white;
    border: none;
    padding: 10px 15px;
    cursor: pointer;
  }
  
  .test-menu {
    display: none;
    position: absolute;
    background-color: white;
    min-width: 200px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    z-index: 100;
  }
  
  .test-menu.open {
    display: block;
  }
  
  .test-item {
    position: relative;
  }
  
  .test-parent {
    display: block;
    padding: 10px 15px;
    text-decoration: none;
    color: #333;
  }
  
  .test-icon {
    position: absolute;
    right: 10px;
    top: 10px;
    transition: transform 0.3s;
  }
  
  .test-item.active .test-icon {
    transform: rotate(90deg);
  }
  
  .test-submenu {
    display: none;
    padding-left: 15px;
    background-color: #f5f5f5;
  }
  
  .test-item.active .test-submenu {
    display: block;
  }
  
  .test-submenu a {
    display: block;
    padding: 8px 15px;
    text-decoration: none;
    color: #555;
  }
</style>

<h2>Dropdown Test Page</h2>
<p>This page tests the multilevel dropdown functionality in isolation.</p>

<div class="test-navbar">
  <div class="test-logo">Test Logo</div>
  
  <div class="test-nav">
    <button id="testButton" class="test-button">Test Menu ▾</button>
    <div id="testMenu" class="test-menu">
      <div class="test-item">
        <a href="#" class="test-parent">Values</a>
        <span class="test-icon">▸</span>
        <div class="test-submenu">
          <a href="#">Self-awareness</a>
          <a href="#">Consciousness</a>
          <a href="#">Personal values</a>
        </div>
      </div>
      
      <div class="test-item">
        <a href="#" class="test-parent">Purpose</a>
        <span class="test-icon">▸</span>
        <div class="test-submenu">
          <a href="#">Life purpose</a>
          <a href="#">Global impact</a>
          <a href="#">Community contribution</a>
        </div>
      </div>
      
      <div class="test-item">
        <a href="#" class="test-parent">Health</a>
        <span class="test-icon">▸</span>
        <div class="test-submenu">
          <a href="#">Fitness</a>
          <a href="#">Nutrition</a>
          <a href="#">Sleep</a>
        </div>
      </div>
    </div>
  </div>
</div>

<script>
  document.addEventListener('DOMContentLoaded', function() {
    // Main dropdown toggle
    const testButton = document.getElementById('testButton');
    const testMenu = document.getElementById('testMenu');
    
    testButton.addEventListener('click', function(e) {
      e.preventDefault();
      testMenu.classList.toggle('open');
    });
    
    // Close when clicking outside
    document.addEventListener('click', function(e) {
      if (!testButton.contains(e.target) && !testMenu.contains(e.target)) {
        testMenu.classList.remove('open');
      }
    });
    
    // Submenu toggles
    const testItems = document.querySelectorAll('.test-item');
    
    testItems.forEach(item => {
      const testIcon = item.querySelector('.test-icon');
      
      testIcon.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        item.classList.toggle('active');
      });
    });
  });
</script>
