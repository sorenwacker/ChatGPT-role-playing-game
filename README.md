# ChatGPT role playing game

Experience an immersive and dynamic adventure with this captivating GitHub project: "AI-Driven Role Playing Game Master". Leveraging the sophisticated capabilities of GPT-3.5, we've transformed artificial intelligence into an interactive, virtual game master for pen and paper role-playing games.

This innovative tool grants you unparalleled freedom, offering the ability to engage in virtually any universe you desire, from the legendary landscapes of Dungeons & Dragons to the action-packed world of Marvel, or even the mystical realm of Das Schwarze Auge. Simply brief the AI about your chosen universe, and watch as it masterfully takes you through the intricacies of character generation.

Once your unique character is forged, you're ready to embark on your bespoke adventure. This smart AI will intricately weave stories tailored to your choices, lending an unpredictable and thrilling layer to your role-playing experience.

Whether you're a seasoned role-player or a curious beginner, the "AI-Driven Role Playing Game Master" opens up a new world of limitless, AI-guided storytelling. It's not just a game, it's your personalized epic.


# Requirements

Store your openai API key as environment variable.

    export OPENAI_API_KEY='<your-key>'

## Install the requirements

    conda env create --file environment.yml
    conda activate chatbot
    cd frontend && npm install
    
## Start the game

### Start the backend

    ./backend/start.sh
   
### Start the frontend

    cd frontend && npm start

