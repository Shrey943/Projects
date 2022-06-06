package com.example.credence;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class UpdateActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_update);

        TextView beliefT = findViewById(R.id.belief);

        final EditText text1 = findViewById(R.id.editText1);
        final EditText text2 = findViewById(R.id.editText2);

        Button submit = findViewById(R.id.submit2);

        Intent intent = getIntent();

        String ID = intent.getStringExtra("ID");
        final int id = Integer.parseInt(ID);

        final SharedPreferences shrd = getSharedPreferences("demo", MODE_PRIVATE);
        String belief = shrd.getString("belief"+id,"Belief");

        final float per = shrd.getFloat("per"+id,(float)25.55);
//        final float oldPer = shrd.getFloat("oldPer"+id,(float)25.55);

        beliefT.setText(belief);

        submit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                final String Text1 = text1.getText().toString();
                final String Text2 = text2.getText().toString();

                if( Text1.length() == 0 || Text2.length() == 0   ){
                    Toast toast = Toast.makeText(UpdateActivity.this,"Values can't be empty",Toast.LENGTH_SHORT);
                    toast.show();
                }
                else if (Float.parseFloat(Text2) >= 100 || Float.parseFloat(Text2) <= 0 ||Float.parseFloat(Text1) >= 100 ||Float.parseFloat(Text1)<=0 ){
                    Toast toast = Toast.makeText(UpdateActivity.this,"Values in percentage must lie between 0 to 100 only.",Toast.LENGTH_SHORT);
                    toast.show();
                }
                else{
                    float N1 = per/100;
                    float N2 = Float.parseFloat(Text1)/100;
                    float N3 = Float.parseFloat(Text2)/100;
                    float a = N1/(1-N1);
                    float b = N2/N3;
                    float c = 1 + a*b;
                    float d = a*b/c;

                    float updatedPer1 = d*100;
                    float updatedPer = (float) (Math.round(updatedPer1*10.0)/10.0);
                    if(updatedPer<=0 || updatedPer>=100){
                        Toast toast = Toast.makeText(UpdateActivity.this,"Credence can't be 0 or 100",Toast.LENGTH_SHORT);
                        toast.show();
                    }
                    else {


                        SharedPreferences.Editor editor = shrd.edit();

                        editor.putFloat("per" + id, updatedPer);
                        editor.apply();

                        Intent intent1 = new Intent(UpdateActivity.this, MainActivity.class);
                        startActivity(intent1);
                        Toast toast = Toast.makeText(UpdateActivity.this, "updated credence: " + updatedPer + "%", Toast.LENGTH_LONG);
                        toast.show();
                    }
                }


            }});



    }
    @Override
    public void onBackPressed(){
        Intent intent = new Intent(UpdateActivity.this,MainActivity.class);
        startActivity(intent);
    }
}