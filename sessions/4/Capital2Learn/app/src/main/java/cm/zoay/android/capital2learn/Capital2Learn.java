package cm.zoay.android.capital2learn;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import cm.zoay.android.capital2learn.utils.Utils;


public class Capital2Learn extends Activity {

    private EditText country = null;
    private Button goButton = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_capital2_learn);

        country = (EditText) findViewById(R.id.country);
        goButton = (Button) findViewById(R.id.goButton);

        // adding a listener
        goButton.setOnClickListener(goButtonlistener);
    }

    private View.OnClickListener goButtonlistener = new View.OnClickListener() {
        @Override
        public void onClick(View v) {
            Utils.message(getApplicationContext(), Utils.ucfirst(country.getText().toString()));
        }
    };
}
