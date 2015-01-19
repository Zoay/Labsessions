package cm.zoay.android.capital2learn.utils;

import android.content.Context;
import android.widget.Toast;

/**
 * Created by zoay on 19/01/15.
 */
public class Utils {

    public static void message(Context context, String message)
    {
        Toast.makeText(context, message, Toast.LENGTH_LONG).show();
    }

    public static String ucfirst(String str)
    {
        if(str.length() == 0) return str;
        return str.substring(0, 1).toUpperCase() + str.substring(1).toLowerCase();
    }
}
