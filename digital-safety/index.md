[← Back to Home](../)
# Digital Safety

## What is Digital Safety?

Digital safety encompasses protecting your online identity, data, privacy, and digital wellbeing from cyber threats, data breaches, surveillance, and digital manipulation. This includes technical security measures (strong passwords, secure connections), privacy practices (data minimisation, platform settings), and behavioural awareness (recognising scams, managing digital consumption). The scope spans from basic password hygiene to sophisticated threat modelling, covering everything from preventing identity theft to maintaining mental health in digital environments.

Digital safety is distinct from but overlaps with productivity (digital organisation) and wellbeing (screen time management). This guide focuses specifically on protection against threats rather than broader questions of digital minimalism or algorithmic manipulation, which are covered in our [Media Diet]({{ site.baseurl }}/media-diet/) and [Consumptive Leisure]({{ site.baseurl }}/consumptive-leisure/) guides.

## Why Digital Safety Matters

Digital safety serves as a foundation for confident participation in the modern digital economy. Effective protection prevents financial losses from fraud and identity theft <span class="info-icon" onclick="showReasoning('research-key-1')">i</span>, whilst preserving personal privacy from corporate surveillance and data harvesting <span class="info-icon" onclick="showReasoning('research-key-2')">i</span>. Poor digital safety practices can result in significant financial losses, privacy violations, reputational damage, and exposure to sophisticated manipulation techniques <span class="info-icon" onclick="showReasoning('research-key-3')">i</span>.

Beyond individual protection, digital safety enables full participation in online services, from banking to healthcare, without excessive vulnerability to various cyber threats that continue to evolve in sophistication and scale.

## Digital Safety Values

Your optimal approach to digital safety depends on what aspects you value most. This guide balances two core values, with percentages indicating the relative weight given to each in our recommendations.

For personalised recommendations based on your unique priorities, visit [Digital Safety Personalised]({{ site.baseurl }}/digital-safety/personalised), where you can adjust these value weightings to see which interventions work best for your specific goals and preferences.

### Comprehensive Security (70%)
Minimising exposure to cyber threats, data breaches, privacy violations, and digital fraud through systematic security measures, privacy controls, and threat awareness. People who prioritise this value focus on thorough protection across devices and platforms, proactive security practices, and evidence-based methods for reducing various categories of digital risk including financial fraud, identity theft, surveillance, and malware. This approach involves learning about emerging threats, implementing multiple layers of protection, and accepting some inconvenience or reduced functionality in exchange for stronger security.

### Usability and Convenience (30%)
Maintaining digital functionality and ease of use whilst achieving reasonable security. This encompasses the ability to use desired platforms, services, and features without excessive security-related friction, complexity, or technical barriers. Those who prioritise this value seek protective measures that integrate seamlessly into existing digital workflows rather than comprehensive systems that may significantly impact user experience, require extensive technical knowledge, or limit access to preferred services and features.

## Benchmarks by Level

Research reveals that most people have very limited engagement with digital safety practices, with significant barriers including lack of awareness, mistrust of security tools, and complexity concerns. Studies show that only 36% of Americans use password managers, 32% use VPNs, and 41% enable two-factor authentication for all accounts. Common barriers include cost (22% find security tools too expensive), complexity (20% don't understand benefits), and trust issues (65% don't trust password managers despite their benefits). These patterns mean that even modest achievements in digital safety represent higher population percentiles than might initially be expected.

### Level 1: Awareness

**Comprehensive Security**: Understand current digital vulnerabilities through basic assessment of password security, device protection, and online habits <span class="info-icon" onclick="showReasoning('level1-security')">i</span>

**Usability and Convenience**: Assess current digital workflows and identify security gaps that don't require significant changes to existing habits <span class="info-icon" onclick="showReasoning('level1-convenience')">i</span>

### Level 2: Foundation (80th percentile capability)

**Comprehensive Security**: Use unique passwords with a password manager for all important accounts, enable 2FA on financial and email accounts, recognise and avoid obvious phishing attempts, keep devices updated with security patches, and use basic privacy settings on social media platforms <span class="info-icon" onclick="showReasoning('level2-security')">i</span>

**Usability and Convenience**: Implement security measures that require minimal daily management through automated tools like browser-integrated password managers and automatic updates. Maintain access to preferred platforms and services while achieving reasonable protection against common threats <span class="info-icon" onclick="showReasoning('level2-convenience')">i</span>

### Level 3: Proficiency (95th percentile capability)

**Comprehensive Security**: Comprehensive password management across all accounts, 2FA enabled on all critical services, reliable recognition of sophisticated phishing attempts, thoughtful privacy settings across all platforms, quarterly review of account security and permissions, and occasional use of encrypted messaging for sensitive conversations <span class="info-icon" onclick="showReasoning('level3-security')">i</span>

**Usability and Convenience**: Streamlined security workflows using premium tools that balance protection with functionality. Minimal disruption to digital habits while maintaining strong security across personal and professional digital activities <span class="info-icon" onclick="showReasoning('level3-convenience')">i</span>

### Level 4: Excellence (99th percentile capability)

**Comprehensive Security**: Personal threat assessment considering individual risk factors, hardware security keys for most important accounts, regular VPN usage for privacy protection, consistent encrypted communication practices, systematic approach to monitoring account activity and responding to security alerts, and careful management of digital footprint across platforms <span class="info-icon" onclick="showReasoning('level4-security')">i</span>

**Usability and Convenience**: Highly efficient security systems that enhance rather than hinder productivity through advanced automation and integration. Seamless protection across all digital activities with minimal daily security management required <span class="info-icon" onclick="showReasoning('level4-convenience')">i</span>

### Level 5: Mastery (99.9th percentile capability)

**Comprehensive Security**: Systematic personal security planning based on individual threat landscape, sophisticated authentication and privacy protection across all digital activities, comprehensive approach to digital privacy including selective platform usage, proactive security monitoring with clear response procedures for suspicious activity, and serves as informal security advisor for family and friends <span class="info-icon" onclick="showReasoning('level5-security')">i</span>

**Usability and Convenience**: Highly sophisticated but transparent security infrastructure that provides maximum protection with minimal user friction. Advanced automation and security systems that maintain full functionality while providing comprehensive protection against sophisticated threats <span class="info-icon" onclick="showReasoning('level5-convenience')">i</span>

## Levels
- [Level 1: Awareness](level-1) *(under development)*
- [Level 2: Foundation](level-2) *(under development)*
- [Level 3: Proficiency](level-3) *(under development)*
- [Level 4: Excellence](level-4) *(under development)*
- [Level 5: Mastery](level-5) *(under development)*
- [Digital Safety Personalised]({{ site.baseurl }}/digital-safety/personalised) *(under development)*

[← Back to Life Levels Home](../)

<style>
.info-icon {
    background-color: #155799;
    color: white;
    border-radius: 50%;
    width: 18px;
    height: 18px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 12px;
    cursor: pointer;
    transition: background-color 0.3s;
    user-select: none;
    margin-left: 3px;
}

.info-icon:hover {
    background-color: #0d47a1;
}

.reasoning-popup {
    display: none;
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: white;
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 20px;
    max-width: 500px;
    width: 90%;
    box-shadow: 0 4px 20px rgba(0,0,0,0.15);
    z-index: 1000;
}

.reasoning-popup.visible {
    display: block;
}

.popup-header {
    font-weight: bold;
    margin-bottom: 10px;
    color: #155799;
}

.popup-close {
    position: absolute;
    top: 10px;
    right: 15px;
    background: none;
    border: none;
    font-size: 20px;
    cursor: pointer;
    color: #666;
}

.popup-close:hover {
    color: #333;
}

.popup-overlay {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.5);
    z-index: 999;
}

.popup-overlay.visible {
    display: block;
}
</style>

<!-- Popup overlay -->
<div class="popup-overlay" id="popupOverlay" onclick="hideReasoning()"></div>

<!-- Reasoning popup -->
<div class="reasoning-popup" id="reasoningPopup">
    <button class="popup-close" onclick="hideReasoning()">×</button>
    <div class="popup-header" id="popupHeader"></div>
    <div id="popupContent"></div>
</div>

<script>
// Research data for info buttons
const researchData = {
    'research-key-1': {
        title: 'Financial Impact Research',
        content: 'Identity theft and cyber fraud create substantial financial losses for individuals. The average cyber insurance claim rose from $145,000 in 2019 to $359,000 in 2020, indicating the growing financial impact of digital threats. Studies show that people with password managers were less likely to experience identity or credential theft (17% affected compared to 32% of those without). <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8853293/" target="_blank">View research</a>'
    },
    'research-key-2': {
        title: 'Privacy Surveillance Research', 
        content: 'Research shows that 73% of people believe organisations gather their personal information without their knowledge, and 77% of Americans have little to no trust in social media leaders regarding data protection. Studies indicate that social media platforms engage in "vast surveillance of consumers" with inadequate privacy controls, collecting extensive personal data for commercial exploitation. <a href="https://www.ftc.gov/news-events/news/press-releases/2024/09/ftc-staff-report-finds-large-social-media-video-streaming-companies-have-engaged-vast-surveillance" target="_blank">View FTC report</a>'
    },
    'research-key-3': {
        title: 'Digital Threat Consequences Research',
        content: 'Cybercrime cost the global economy just under $1 trillion in 2020, with 85% of data breaches involving human factors. Research shows that 26% of people have experienced at least one cyber incident, with consequences including financial loss, identity theft, and reputational damage. Poor digital safety practices increase vulnerability to sophisticated threats including deepfakes (experienced by 47% of organisations) and AI-driven attacks. <a href="https://secureframe.com/blog/cybersecurity-statistics" target="_blank">View study</a>'
    },
    
    // Level 1 reasoning
    'level1-security': {
        title: 'Level 1 Security Reasoning',
        content: 'This represents basic awareness appropriate for assessment-level engagement. Research shows significant gaps in basic cybersecurity knowledge, with studies finding that 20% of underserved populations don\'t know about online crime and 31% don\'t know about antivirus software. Level 1 focuses on understanding these fundamental concepts without requiring implementation.'
    },
    'level1-convenience': {
        title: 'Level 1 Convenience Reasoning',
        content: 'Level 1 convenience focuses on assessment without disruption to existing workflows. This acknowledges that 37% of people don\'t think they need security tools and 23% don\'t believe they are secure, indicating that awareness-building must respect current digital habits and preferences.'
    },
    
    // Level 2 reasoning  
    'level2-security': {
        title: 'Level 2 Security Reasoning',
        content: 'This represents 80th percentile achievement based on research showing only 36% of Americans use password managers and 41% enable 2FA for all accounts. Since Level 2 targets the top 20% of the population, achieving comprehensive password management and selective 2FA implementation represents significant improvement over average security practices. Studies demonstrate these measures prevent 99.9% of automated attacks.'
    },
    'level2-convenience': {
        title: 'Level 2 Convenience Reasoning',
        content: 'Level 2 convenience emphasises security measures that integrate with existing workflows. Research shows 51% of people rely on memorisation for passwords, making browser-integrated password managers a significant but manageable improvement. Automatic updates and basic privacy settings provide substantial protection with minimal daily interaction required.'
    },
    
    // Level 3 reasoning
    'level3-security': {
        title: 'Level 3 Security Reasoning',
        content: 'This represents 95th percentile capability (top 5%) based on population research. While 41% use 2FA for some accounts, comprehensive 2FA across all critical services, sophisticated phishing recognition, and systematic security reviews represent advanced practices achieved by very few people. Quarterly security reviews indicate proactive rather than reactive security management.'
    },
    'level3-convenience': {
        title: 'Level 3 Convenience Reasoning',
        content: 'Level 3 convenience focuses on streamlined workflows using premium tools that balance protection with functionality. This level represents users who have moved beyond basic security to sophisticated but manageable systems that enhance rather than hinder digital productivity.'
    },
    
    // Level 4 reasoning
    'level4-security': {
        title: 'Level 4 Security Reasoning',
        content: 'This represents 99th percentile capability (top 1%) incorporating advanced practices like personal threat assessment and hardware security keys. With only 32% of Americans using VPNs and most using free/less secure options, regular strategic VPN usage plus systematic security monitoring represents sophisticated personal security practices achieved by very few individuals.'
    },
    'level4-convenience': {
        title: 'Level 4 Convenience Reasoning',
        content: 'Level 4 convenience represents highly efficient security systems that enhance productivity through advanced automation. This level indicates security expertise that allows for sophisticated protection without daily management overhead, representing the top 1% of personal security implementations.'
    },
    
    // Level 5 reasoning
    'level5-security': {
        title: 'Level 5 Security Reasoning',
        content: 'This represents 99.9th percentile capability (top 0.1%, ~340,000 Americans) with systematic personal security planning and comprehensive threat management. This level includes serving as informal security advisor, indicating expertise sufficient to guide others while maintaining sophisticated personal security practices across all digital activities.'
    },
    'level5-convenience': {
        title: 'Level 5 Convenience Reasoning',
        content: 'Level 5 convenience represents sophisticated security infrastructure that provides maximum protection with minimal user friction. This level indicates mastery where advanced security becomes transparent to daily use, representing the most sophisticated personal digital safety implementations achievable.'
    }
};

function showReasoning(key) {
    const data = researchData[key];
    if (data) {
        document.getElementById('popupHeader').textContent = data.title;
        document.getElementById('popupContent').innerHTML = data.content;
        document.getElementById('popupOverlay').classList.add('visible');
        document.getElementById('reasoningPopup').classList.add('visible');
    }
}

function hideReasoning() {
    document.getElementById('popupOverlay').classList.remove('visible');
    document.getElementById('reasoningPopup').classList.remove('visible');
}

// Close popup with Escape key
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        hideReasoning();
    }
});
</script>
