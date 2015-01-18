package af.cmr.zoay.capital2learn;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;


public class Capital2LearnActivity extends Activity {

    private EditText countryName = null;
    private Button goButton = null;

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_capital2_learn);

        countryName = (EditText) findViewById(R.id.countryName);
        goButton = (Button) findViewById(R.id.goButton);

        goButton.setOnClickListener(goButtonListener);
    }

    private View.OnClickListener goButtonListener = new View.OnClickListener() {
        @Override
        public void onClick(View v)
        {
            printToast(ucfirst(countryName.getText().toString()));
        }
    };

    private void printToast(CharSequence text)
    {
        Toast toast = Toast.makeText(getApplicationContext(), text, Toast.LENGTH_LONG);
        toast.show();
    }

    /*
     This method capitalize the first letter of the
     string given in input
     */

    private String ucfirst(String origin)
    {
        if(origin.length() == 0)
        {
            return origin;
        }
        return origin.substring(0, 1).toUpperCase() + origin.substring(1).toLowerCase();
    }
}
