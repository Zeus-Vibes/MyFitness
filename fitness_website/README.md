# Fitness Website

A comprehensive Django-based fitness website that provides workout plans, exercise library, diet plans, health calculators, and a powerful admin panel for content management.

## Features

### User Management
- User registration and authentication
- Custom user profiles with fitness information
- Role-based access control (User, Trainer, Admin)
- Profile management with fitness goals and activity levels

### Workout System
- Browse workout plans by difficulty and goals
- Detailed exercise library with YouTube video demonstrations
- Structured workout sessions with sets, reps, and rest times
- Personal workout tracking (for logged-in users)

### Nutrition System
- Diet plans with macro breakdowns
- Food database with nutritional information
- Meal planning with calorie tracking
- Personal diet plan management

### Health Calculators
- BMI Calculator with category classification
- Daily Calorie Calculator using Mifflin-St Jeor equation
- Activity level-based TDEE calculation

### Admin Panel (NEW!)
- **Comprehensive Dashboard** with statistics and analytics
- **User Management** - Full CRUD operations for users
- **Workout Management** - Create and manage workout plans
- **Exercise Library** - Add exercises with video demonstrations
- **Diet Plan Management** - Create nutrition plans with macro tracking
- **Search & Filtering** - Advanced search across all content
- **Role-Based Access** - Secure admin-only access
- **Responsive Design** - Beautiful, mobile-friendly interface

## Installation

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```
   python manage.py migrate
   ```

4. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

5. Populate with sample data:
   ```
   python manage.py populate_data
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage

### Public Access
- **Home:** `http://127.0.0.1:8000/`
- **Workouts:** `http://127.0.0.1:8000/workouts/`
- **Exercises:** `http://127.0.0.1:8000/workouts/exercises/`
- **Diet Plans:** `http://127.0.0.1:8000/nutrition/`
- **BMI Calculator:** `http://127.0.0.1:8000/calculators/bmi/`
- **Calorie Calculator:** `http://127.0.0.1:8000/calculators/calories/`

### Admin Access
- **Admin Panel:** `http://127.0.0.1:8000/admin-panel/`
- **Django Admin:** `http://127.0.0.1:8000/admin/`
- **Default Credentials:** username: `admin` / password: `admin`

### User Features
- Register/Login at `/accounts/register/` or `/accounts/login/`
- Manage profile at `/accounts/profile/`
- Track workouts and diet plans
- Use health calculators

### Admin Features
- Access admin panel (Admin/Superuser only)
- Manage users with full CRUD operations
- Create and edit workout plans
- Add exercises with YouTube videos
- Design diet plans with macro tracking
- View platform statistics and analytics
- Search and filter all content

## User Roles

### Regular User
- Browse workout plans and exercises
- View diet plans
- Use calculators
- Track personal fitness journey

### Trainer (Future)
- Create workout plans
- Add exercises
- Manage assigned users

### Administrator
- Full system access
- User management
- Content management
- Platform analytics
- System configuration

## Project Structure

```
fitness_website/
├── accounts/          # User management
├── workouts/          # Workout plans and exercises
├── nutrition/         # Diet plans and nutrition
├── calculators/       # BMI and calorie calculators
├── templates/         # HTML templates
└── fitness_website/   # Main project settings
```

## Models

### User Model (CustomUser)
- Extended Django user with fitness-specific fields
- Age, height, weight, fitness goals, activity level

### Workout Models
- WorkoutPlan: Structured fitness programs
- Exercise: Individual exercises with video links
- WorkoutSession: Daily workout sessions
- WorkoutExercise: Exercise details within sessions

### Nutrition Models
- DietPlan: Nutrition programs with macro targets
- Food: Food items with nutritional data
- Meal: Meal plans within diet programs
- MealFood: Food quantities in meals

### Calculator Models
- BMICalculation: BMI calculation history
- CalorieCalculation: TDEE calculation history

## Technologies Used

- Django 5.x
- Bootstrap 5 for responsive UI
- SQLite database (default)
- YouTube integration for exercise videos

## Future Enhancements

- Progress tracking and analytics
- Social features and community
- Mobile app integration
- Advanced meal planning
- Workout plan customization
- Integration with fitness trackers