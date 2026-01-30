from django.core.management.base import BaseCommand
from workouts.models import Exercise, WorkoutPlan, WorkoutSession, WorkoutExercise
from nutrition.models import DietPlan, Food, Meal, MealFood

class Command(BaseCommand):
    help = 'Populate database with sample fitness data'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample exercises...')
        
        # Create sample exercises
        exercises_data = [
            {
                'name': 'Push-ups',
                'description': 'Classic bodyweight exercise for chest, shoulders, and triceps',
                'muscle_groups': 'Chest, Shoulders, Triceps',
                'equipment_needed': 'None',
                'youtube_url': 'https://www.youtube.com/watch?v=IODxDxX7oi4',
                'instructions': '1. Start in plank position\n2. Lower body until chest nearly touches floor\n3. Push back up to starting position\n4. Repeat'
            },
            {
                'name': 'Squats',
                'description': 'Fundamental lower body exercise',
                'muscle_groups': 'Quadriceps, Glutes, Hamstrings',
                'equipment_needed': 'None',
                'youtube_url': 'https://www.youtube.com/watch?v=aclHkVaku9U',
                'instructions': '1. Stand with feet shoulder-width apart\n2. Lower body as if sitting back into chair\n3. Keep chest up and knees behind toes\n4. Return to standing position'
            },
            {
                'name': 'Deadlifts',
                'description': 'Compound exercise for posterior chain',
                'muscle_groups': 'Hamstrings, Glutes, Lower Back',
                'equipment_needed': 'Barbell or Dumbbells',
                'youtube_url': 'https://www.youtube.com/watch?v=ytGaGIn3SjE',
                'instructions': '1. Stand with feet hip-width apart\n2. Hinge at hips and lower weight\n3. Keep back straight and chest up\n4. Drive through heels to return to standing'
            },
            {
                'name': 'Plank',
                'description': 'Core strengthening exercise',
                'muscle_groups': 'Core, Shoulders',
                'equipment_needed': 'None',
                'youtube_url': 'https://www.youtube.com/watch?v=ASdvN_XEl_c',
                'instructions': '1. Start in push-up position\n2. Lower to forearms\n3. Keep body in straight line\n4. Hold position'
            },
            {
                'name': 'Burpees',
                'description': 'Full-body cardio exercise',
                'muscle_groups': 'Full Body',
                'equipment_needed': 'None',
                'youtube_url': 'https://www.youtube.com/watch?v=auBLPXO8Fww',
                'instructions': '1. Start standing\n2. Drop into squat, place hands on floor\n3. Jump feet back to plank\n4. Do push-up, jump feet forward\n5. Jump up with arms overhead'
            }
        ]
        
        exercises = []
        for ex_data in exercises_data:
            exercise, created = Exercise.objects.get_or_create(
                name=ex_data['name'],
                defaults=ex_data
            )
            exercises.append(exercise)
            if created:
                self.stdout.write(f'Created exercise: {exercise.name}')

        # Create sample workout plan
        self.stdout.write('Creating sample workout plan...')
        
        workout_plan, created = WorkoutPlan.objects.get_or_create(
            name='Beginner Full Body Workout',
            defaults={
                'description': 'A comprehensive 4-week beginner workout plan focusing on all major muscle groups',
                'difficulty_level': 'beginner',
                'duration_weeks': 4,
                'goal': 'strength'
            }
        )
        
        if created:
            # Create workout sessions
            session1 = WorkoutSession.objects.create(
                workout_plan=workout_plan,
                name='Upper Body Focus',
                day_number=1,
                description='Focus on chest, shoulders, and arms'
            )
            
            session2 = WorkoutSession.objects.create(
                workout_plan=workout_plan,
                name='Lower Body Focus',
                day_number=2,
                description='Focus on legs and glutes'
            )
            
            session3 = WorkoutSession.objects.create(
                workout_plan=workout_plan,
                name='Full Body Circuit',
                day_number=3,
                description='High-intensity full body workout'
            )
            
            # Add exercises to sessions
            WorkoutExercise.objects.create(
                session=session1,
                exercise=exercises[0],  # Push-ups
                sets=3,
                reps='8-12',
                rest_time='60 seconds',
                order=1
            )
            
            WorkoutExercise.objects.create(
                session=session1,
                exercise=exercises[3],  # Plank
                sets=3,
                reps='30 seconds',
                rest_time='30 seconds',
                order=2
            )
            
            WorkoutExercise.objects.create(
                session=session2,
                exercise=exercises[1],  # Squats
                sets=3,
                reps='12-15',
                rest_time='60 seconds',
                order=1
            )
            
            WorkoutExercise.objects.create(
                session=session3,
                exercise=exercises[4],  # Burpees
                sets=3,
                reps='5-8',
                rest_time='90 seconds',
                order=1
            )
            
            self.stdout.write(f'Created workout plan: {workout_plan.name}')

        # Create sample foods
        self.stdout.write('Creating sample foods...')
        
        foods_data = [
            {'name': 'Chicken Breast', 'calories_per_100g': 165, 'protein_per_100g': 31, 'carbs_per_100g': 0, 'fat_per_100g': 3.6},
            {'name': 'Brown Rice', 'calories_per_100g': 111, 'protein_per_100g': 2.6, 'carbs_per_100g': 23, 'fat_per_100g': 0.9},
            {'name': 'Broccoli', 'calories_per_100g': 34, 'protein_per_100g': 2.8, 'carbs_per_100g': 7, 'fat_per_100g': 0.4},
            {'name': 'Salmon', 'calories_per_100g': 208, 'protein_per_100g': 25, 'carbs_per_100g': 0, 'fat_per_100g': 12},
            {'name': 'Sweet Potato', 'calories_per_100g': 86, 'protein_per_100g': 1.6, 'carbs_per_100g': 20, 'fat_per_100g': 0.1},
            {'name': 'Greek Yogurt', 'calories_per_100g': 59, 'protein_per_100g': 10, 'carbs_per_100g': 3.6, 'fat_per_100g': 0.4},
        ]
        
        foods = []
        for food_data in foods_data:
            food, created = Food.objects.get_or_create(
                name=food_data['name'],
                defaults=food_data
            )
            foods.append(food)
            if created:
                self.stdout.write(f'Created food: {food.name}')

        # Create sample diet plan
        self.stdout.write('Creating sample diet plan...')
        
        diet_plan, created = DietPlan.objects.get_or_create(
            name='Balanced Nutrition Plan',
            defaults={
                'description': 'A well-balanced diet plan for general health and fitness',
                'goal': 'maintenance',
                'daily_calories': 2000,
                'protein_percentage': 25,
                'carbs_percentage': 50,
                'fat_percentage': 25
            }
        )
        
        if created:
            # Create sample meals
            breakfast = Meal.objects.create(
                diet_plan=diet_plan,
                meal_type='breakfast',
                name='Protein-Rich Breakfast',
                description='High protein breakfast to start your day'
            )
            
            lunch = Meal.objects.create(
                diet_plan=diet_plan,
                meal_type='lunch',
                name='Balanced Lunch',
                description='Balanced meal with protein, carbs, and vegetables'
            )
            
            # Add foods to meals
            MealFood.objects.create(meal=breakfast, food=foods[5], quantity_grams=200)  # Greek Yogurt
            MealFood.objects.create(meal=lunch, food=foods[0], quantity_grams=150)  # Chicken Breast
            MealFood.objects.create(meal=lunch, food=foods[1], quantity_grams=100)  # Brown Rice
            MealFood.objects.create(meal=lunch, food=foods[2], quantity_grams=100)  # Broccoli
            
            self.stdout.write(f'Created diet plan: {diet_plan.name}')

        self.stdout.write(self.style.SUCCESS('Successfully populated database with sample data!'))